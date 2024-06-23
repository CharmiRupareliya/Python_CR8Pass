import random
import string
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)   # Initializing colorama to automatically reset colors after each print.
print()
print(Fore.YELLOW + Style.BRIGHT +"Welcome to CR8Pass: Your shield for bulletproof passwords.")
print()

# Function to generate a random password.
def generate_password(min_length, numbers=True, special_characters=True):
    # Defining sets of characters for password generation
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Starting with letters and conditionally adding digits and special characters
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""  # Initializing the password as an empty string

    # Loop to generate a password of at least the minimum length
    while len(pwd) < min_length:
        new_char = random.choice(characters)   # Adding a random character from the selected set
        pwd += new_char

        # Ensuring at least one digit is included if numbers are requested
        if numbers and not any(char in digits for char in pwd):
            pwd += random.choice(digits)

        # Ensuring at least one special character is included if special characters are requested
        if special_characters and not any(char in special for char in pwd):
            pwd += random.choice(special)

    return pwd


min_length = int(input("Enter length (min 12) for your bulletproof password : "))
has_number = input("Integrate serial numbers for enhanced password security? (y/n) ?").lower() == "y"
has_special = input("Use special symbols as secret signals in your password (y/n)? ? ").lower() =="y"

thank_you_messages = [
    Fore.GREEN + "Mission accomplished!\U0001F3AF Your password is ready for deployment.",
    Fore.MAGENTA + "Your password is now a well-defended fortress. Stand strong!\U0001F60E	",
    Fore.CYAN + "Soldier\U0001F46E, you've secured your digital base with a bulletproof password!",
    Fore.LIGHTBLUE_EX + "Congratulations, recruit!\U0001F916 You've created a password worthy of the front lines.",
    Fore.LIGHTGREEN_EX + "Looks like you've scrambled the enemy codebreakers with that password! Good work!\U0001FAE1",
]

pwd = generate_password(min_length, has_number, has_special)   # Generating the password based on user inputs.
print("The generated password is :",Fore.RED + Style.BRIGHT + pwd)
print()
print(random.choice(thank_you_messages))