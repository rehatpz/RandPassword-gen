
"""
Random Password Generator

This program generates strong, random passwords of specified lengths and complexity.
It prompts the user to input the desired password length and the number of passwords to generate.
"""
import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase  # Set of lowercase letters
    uppercase = string.ascii_uppercase  # Set of uppercase letters
    digits = string.digits  # Set of digits (0-9)
    special_chars = string.punctuation  # Set of special characters

    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Generate password using random.choice
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


while True:
  print("Welcome to Random Password Generator!")
  print("Here you can get crazy with the number of passwords you want to generate. Enjoy!\n")

# Input validation loop for password length
  while True:
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length <= 0:
            print("Please enter a positive value for password length.")
        else:
            break  # Break out of the loop when valid input is received
    except ValueError:
        print("Please enter a valid integer for password length.")

# Input validation loop for the number of passwords to generate
  while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a positive value for the number of passwords.")
            else:
                break  # Break out of the loop when valid input is received
        except ValueError:
            print("Please enter a valid integer for the number of passwords.")
# Generate and print the requested number of passwords
  for i in range(num_passwords):
    generated_password = generate_password(password_length)
    print(f"Password {i+1}: {generated_password}")

# Ask user if they want to continue or exit
  choice = input("Do you want to generate more passwords? (yes/no): ").lower()
  if choice != 'yes':
        print("Thank you for using the password generator. Have a safe browsing!")
        break  # Exit the loop and end the program








