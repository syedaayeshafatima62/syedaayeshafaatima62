from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "greetings": ["Hey there! 👋", "Hi! How’s it going?", "Hello! 😊", "Hey! What’s up?"],
    "food": [
        "You could try making pasta or maybe a salad 🥗.",
        "How about some biryani or a sandwich?",
        "Try something light like a smoothie or some noodles 🍜.",
        "Maybe pizza tomorrow? 🍕"
    ],
    "ok": [
        "Alright! 👍",
        "Got it 😊",
        "Okay, noted!",
        "Sure thing!"
    ],
    "bye": [
        "Goodbye! 👋 Take care!",
        "See you later 😊",
        "Bye! Have a nice day!",
        "Goodbye, friend!"
    ],
    "default": [
        "Interesting! Tell me more 🤔",
        "That sounds nice!",
        "Hmm… I see. Go on!",
        "Really? That’s cool 😄",
        "Can you give me more details on that?"
    ]
}

def get_bot_reply(user_input):
    text = user_input.lower()
    if any(word in text for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greetings"])
    elif any(word in text for word in ["rice", "food", "eat", "hungry", "dinner", "lunch"]):
        return random.choice(responses["food"])
    elif any(word in text for word in ["ok", "okay", "fine"]):
        return random.choice(responses["ok"])
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["bye"])
    else:
        return random.choice(responses["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_bot_reply(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
