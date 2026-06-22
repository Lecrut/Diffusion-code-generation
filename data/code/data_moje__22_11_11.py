import re

def validate_password(password):
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
    samples = ["WeakPass", "ValidPass1!", "Short1!", "NodigitABC!", "NoUpper1!@", "NoSpecial1ABC", "ComplexP@ss9"]
    for sample in samples:
        result = validate_password(sample)
        print(f"{sample}: {result}")