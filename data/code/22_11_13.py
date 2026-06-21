import re

def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "Weak1!",
        "StrongP@ss1",
        "NoSpecial1a",
        "NOdigit1!",
        "ValidP@ss8",
        "Sh0rtP@ss",
        "ValidP@ss!1234"
    ]
    for case in test_cases:
        result = validate_password(case)
        print(f"{case}: {result}")