def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I am CodeBot, your Python chatbot."
    elif user_input == "help":
        return "Try typing: hello, how are you, what is your name, or bye"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can say."

def chatbot():
    print("=== CodeBot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() == "bye":
            break

chatbot()