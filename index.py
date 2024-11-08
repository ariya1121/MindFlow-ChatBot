import nltk
from datetime import datetime
import random

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I assist you?"],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
    "time": ["The current time is: "],
    "what_name": ["My name is MindFlow ChatBot,  always ready to help you resolve any issue!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "I'm here to help with basic queries!"],
}

# Define functions to handle different responses
def get_greeting():
    return random.choice(responses["greeting"])

def get_farewell():
    return random.choice(responses["farewell"])

def get_time():
    return f"{responses['time'][0]} {datetime.now().strftime('%H:%M:%S')}"

def get_default_response():
    return random.choice(responses["default"])

# Function to handle what's your name type questions
def get_what_name():
    return responses["what_name"][0]

# Function to handle basic arithmetic operations
def handle_arithmetic(user_input):
    try:
        result = eval(user_input)
        return f"The answer is: {result}"
    except:
        return "I'm sorry, I can't handle that expression yet. Please try a simpler one."

# Define input processing function
def process_input(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return get_greeting()
    elif any(word in tokens for word in ["bye", "goodbye"]):
        return get_farewell()
    elif "time" in tokens:
        return get_time()
    elif any(word in tokens for word in ["thanks", "thank you"]):
        return responses["thanks"][0]
    elif any(word in tokens for word in ["name", "your name"]):
        return get_what_name()
    else:
        # Check for arithmetic expressions
        response = handle_arithmetic(user_input)
        if response:
            return response
        else:
            return get_default_response()

# Define main chatbot loop
def chatbot():
    print("Chatbot: Hello! I'm here to help with basic queries. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", get_farewell())
            break
        response = process_input(user_input)
        print("Chatbot:", response)

# Run chatbot
chatbot()