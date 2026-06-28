import string

# Some common weak passwords
common_passwords = [
    "password",
    "123456",
    "12345678",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "abc123",
    "welcome",
    "letmein"
]

print("      PASSWORD STRENGTH CHECKER")

password = input("Enter your password: ")

score = 0

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

# Check if password is common
if password.lower() in common_passwords:
    print("\nWarning!")
    print("This is a very common password.")
    print("It can be guessed easily.\n")

# Check password length
if len(password) >= 8:
    score += 1
else:
    print("- Password should be at least 8 characters long.")

# Check every character
for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

    elif ch in string.punctuation:
        has_symbol = True

# Uppercase check
if has_upper:
    score += 1
else:
    print("- Add at least one uppercase letter.")

# Lowercase check
if has_lower:
    score += 1
else:
    print("- Add at least one lowercase letter.")

# Number check
if has_digit:
    score += 1
else:
    print("- Add at least one number.")

# Special character check
if has_symbol:
    score += 1
else:
    print("- Add at least one special character.")

print("Password Score:", score, "/5")

# Decide password strength
if len(password) < 8:
    print("Password Strength: Weak")

elif score == 5:
    print("Password Strength: Strong")

else:
    print("Password Strength: Medium")

# Final message
if score == 5 and password.lower() not in common_passwords:
    print("Excellent! Your password is secure.")
elif score >= 3:
    print("Your password is okay, but it can be improved.")
else:
    print("Your password is not secure. Try making it stronger.")