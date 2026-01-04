from intents import intents

def get_response(user_input):
    user_input = user_input.lower()

    for intent in intents.values():
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent["response"]

    return "Sorry, I didn't understand that. Please ask about admissions, fees, or departments."

print("🎓 ABC University Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    response = get_response(user_input)
    print("Bot:", response)

    if "bye" in user_input or "exit" in user_input:
        break
