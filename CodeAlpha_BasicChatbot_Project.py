# made up code to slow down print message
for char in "Welcome\nI'm Chatty your basic user-friendly Chatbot":
    print(char, end='', flush=True)
    for i in range(100000): pass
print()
print("_"*40)
# Asks User's name for better interactions
name = input("What's your name?: ")
print(f"Heya {name}")

# nested if's for conversations between user and chatbot
user_input = input("You: ")
if user_input == ["hi", "hello", "heya"]:
    print("How are ya")
    user_input = input("You: ")

    if user_input == ["how are you", "Good", "I'm okay", "I'm good, yourself?"]:
        print("I'm a bot but thanks")
    user_input = input("You: ")

    if user_input == ["yh", "yeah", "yep"]:
        print("Oh that's awesome.\nSo how can I help you today?", name)
    user_input_body = input("You: ")

if user_input != "":
    user = input(
                 "Unfortunately I am a prototype with very limited functionality."
                 "\nMy developers are working tirelessly to make me fully operational\n"
                 "Is there something else I can help you with??\nYou:"
                  )
    if user == ["no" or "No"]:
        print("Okay, have a nice day")

# the code still needs some kinks, but I'll have to make use of if - else statements till I get to libraries