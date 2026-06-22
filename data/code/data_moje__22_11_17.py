import re

def is_password_valid(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    samples = ["WeakPass1", "ValidP@ss1", "short1!", "NoDigitsHere!A", "12345678", "Strong@Pass9"]
    for s in samples:
        result = is_password_valid(s)
        print(f"{s}: {result}")