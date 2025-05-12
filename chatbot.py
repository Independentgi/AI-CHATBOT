print("Welcome to MoodMate - Your Emotional Support Bot!")
mode = input("Choose your mode (bot/pet/chill): ").lower()

while True:
    user_input = input("How are you feeling today? ").lower()

    if "sad" in user_input or "upset" in user_input:
        if mode == "bot":
            print("Processing... Analyzing emotions... You are not alone. 🤖")
        elif mode == "pet":
            print("Woof! I'm here! Let's wag those worries away! 🐾")
        elif mode == "chill":
            print("Breathe in... breathe out... Let it go. 🌬️🧘")
    elif "happy" in user_input or "good" in user_input:
        if mode == "bot":
            print("Positive mood detected. Glad to see efficiency in emotions. 🤖")
        elif mode == "pet":
            print("Yay! Let's play fetch with joy! 🐶")
        elif mode == "chill":
            print("Happiness flows like a calm river. 🌊")
    elif "angry" in user_input or "mad" in user_input:
        if mode == "bot":
            print("Warning: High emotion levels. Cooling system activated. 🤖")
        elif mode == "pet":
            print("Grrr... let’s growl it out together! 🐕")
        elif mode == "chill":
            print("Let go of the flame. Be the breeze. 🧘")
    elif "exit" in user_input:
        print("MoodMate says goodbye with good vibes. 🫶")
        break
    else:
        print("Hmm... I didn’t quite catch that emotion. Try describing how you feel.")
