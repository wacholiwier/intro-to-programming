print("EDIZA: Hello! I'm EDIZA. Tell me what's on your mind.")

general_responses = ["Please tell me more.", "How does that make you feel?", "What makes you say that?"]
response_index = 0

while True: 
    message = input("You: ")
    message = message.lower()
    message = message.strip()
    if message == "bye":
        print("EDIZA: Goodbye!")
        break
    elif message == "":
        print("EDIZA: Even a chatbot needs something to go on.")
    else:
        reply = general_responses[response_index]
        print(f"EDIZA: {reply}")
        response_index += 1
        response_index = (response_index) % len(general_responses)

print("Thanks")


    