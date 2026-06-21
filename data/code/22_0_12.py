import re

def validate_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    sample_passwords = [
        "Short1!",
        "nouppercase1!",
        "NOLOWERCASE1!",
        "NoDigit!",
        "NoSpecial1",
        "ValidPass1!",
        "Complex123$",
        "aB3!@#123"
    ]
    for pwd in sample_passwords:
        print(validate_password_strength(pwd))