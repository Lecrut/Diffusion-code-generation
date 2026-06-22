import re

def is_password_valid(password):
    if len(password) < 8:
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    test_cases = ["Pass123!", "short1A!", "AllLower123", "NoDigitsHere!", "ValidP@ss9"]
    for case in test_cases:
        print(f"{case}: {is_password_valid(case)}")