import os
import google.generativeai as genai
from dotenv import load_dotenv


# Load api key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#pick a Model you have accesss to (from your list)
MODEL_NAME = "models/gemini-2.5-flash"

class Chatbot:
    def __init__(self, model_name):
        self.model = genai.GenerativeModel(model_name)
        self.chat = self.model.start_chat(history=[])

    def send_message(self, message):
        response = self.chat.send_message(message)              
        return response.text
if __name__ == "__main__":
    bot = Chatbot(MODEL_NAME)
    print("Welcome to your AI Chatbot!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        reply = bot.send_message(user_input)
        print(f"Bot: {reply}\n")