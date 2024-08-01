import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    
    # Length
    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    
    # Digits
    if re.search(r'[0-9]', password):
        score += 1
    
    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Feedback based on score
    feedback = "Your password is "
    if score <= 2:
        feedback += "very weak. Consider adding more characters, including uppercase, lowercase, digits, and special characters."
    elif score <= 4:
        feedback += "weak. Try to include a variety of character types and increase the length."
    elif score <= 5:
        feedback += "moderate. Adding more character types and increasing the length will make it stronger."
    else:
        feedback += "strong. Good job!"

    return feedback, score

# Example usage
password = input("Enter a password to assess: ")
feedback, score = assess_password_strength(password)
print(f"Password Strength Score: {score}/6")
print(feedback)

