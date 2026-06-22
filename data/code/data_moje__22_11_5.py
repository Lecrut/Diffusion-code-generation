import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "short",
        "nodigitA!",
        "noUpper1!",
        "nospecial1A",
        "ValidP@ss1",
        "Strong!Word9",
        "weak"
    ]
    for pwd in test_cases:
        result = is_valid_password(pwd)
        print(f"{pwd}: {result}")