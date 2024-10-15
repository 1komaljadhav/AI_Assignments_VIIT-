import aiml
import os

# Create a Kernel object
kernel = aiml.Kernel()

# Check if the brain file exists to avoid reloading AIML files
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    # Load the AIML file
    kernel.learn("customer_service.aiml")
    # Save the brain file to avoid reloading the AIML files each time
    kernel.saveBrain("bot_brain.brn")

# Start the chatbot loop
print("Customer Service Chatbot is now running. Type 'bye' to exit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # If the user types 'bye', exit the loop
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    
    # Get bot response
    response = kernel.respond(user_input)
    
    # Display bot's response
    print(f"Bot: {response}")
