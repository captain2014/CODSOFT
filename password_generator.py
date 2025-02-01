import random
import string

def generate_password(length):
    """
    Generate a strong random password of the specified length.
    The password includes uppercase letters, lowercase letters, digits, and special characters.
    """

    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None

    # Define possible character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # Special characters like !@#$%^&*

    # Ensure password contains at least one character from each set
    all_chars = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)

    # Fill the remaining length with random choices from all characters
    password += ''.join(random.choice(all_chars) for _ in range(length - 4))

    # Shuffle the password to avoid predictable patterns
    password = ''.join(random.sample(password, len(password)))

    return password

def main():
    """Main function to run the password generator."""
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            
            if length <= 0:
                print("Please enter a valid positive number.")
                continue

            password = generate_password(length)
            
            if password:
                print(f"Generated Password: {password}")

            # Ask the user if they want another password
            choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Exiting Password Generator. Stay secure!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
