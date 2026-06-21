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
    samples = [
        "Short1!",
        "nouppercase1!",
        "NoLowercase1!",
        "NoDigits!",
        "NoSpecial1",
        "ValidPass1!",
        "12345678",
        "ABCDEFGHI",
        "abcdefghi",
        "A1!b2@c3"
    ]
    for s in samples:
        print(validate_password_strength(s))