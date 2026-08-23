from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


@app.route("/")
def home():
    return "Compass AI Backend is running!"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    return jsonify({
        "answer": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)