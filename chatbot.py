import random
import spacy

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Define a simple list of responses for greetings
GREETING_INPUTS = ["hello", "hi", "greetings", "hey", "hola","thank you"]
GREETING_RESPONSES = ["Hello!", "Hi there!", "Greetings!", "Hey!", "Hola!"]

# Define fallback responses if the bot doesn't understand the query
UNKNOWN_RESPONSES = [
    "I'm sorry, I don't understand.",
    "Can you please rephrase?",
    "I'm not sure about that.",
    "Let's talk about something else."
    
]

def greet(sentence):
    """If the user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if "thank you" in GREETING_INPUTS :
            return "no mention"
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

def generate_response(user_input):
    """Generate a response based on the user's input"""
    # Process the user input with spaCy
    doc = nlp(user_input)
    lemmatized_tokens = [token.lemma_.lower() for token in doc]

    # Detect if the user provides their name
    if "my name is" in user_input.lower():
        # Extract the name from the input
        name = user_input.lower().split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {name}!"

    # Simple responses based on keywords
    elif  "your" in lemmatized_tokens:
        return "My name is Chatbot. How can I help you?"
    elif "weather" in lemmatized_tokens:
        return "I'm not sure, but I hope it's sunny wherever you are!"
    elif "how" in lemmatized_tokens and "you" in lemmatized_tokens:
        return "I'm just a bot, but thank you for asking!"
    elif "help" in lemmatized_tokens:
        return "I'm here to help you! Ask me any question."
    elif "bye" in lemmatized_tokens:
        return "Goodbye! Have a great day!"

    # If no specific response is found
    return random.choice(UNKNOWN_RESPONSES)

def chatbot_response(user_input):
    """Main function to handle the chatbot's response"""
    user_input = user_input.lower()

    # Check if the input is a greeting
    greeting = greet(user_input)
    if greeting:
        return greeting

    # Otherwise, generate a response based on input
    return generate_response(user_input)

# Chatbot conversation loop
if __name__ == "__main__":
    print("Hello! I'm Chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
