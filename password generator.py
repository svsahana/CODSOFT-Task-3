import random
import string


def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_chars

    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        num_passwords = int(input("How many passwords would you like to generate? "))
        if num_passwords <= 0:
            print("Number of passwords must be a positive integer.")
            return

        for _ in range(num_passwords):
            print(generate_password(length, use_uppercase, use_digits, use_special_chars))

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
