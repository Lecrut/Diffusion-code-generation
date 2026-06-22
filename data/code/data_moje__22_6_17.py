import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        return False
    if re.search(r"(.)\1{3,}", password):
        return False
    return True

if __name__ == '__main__':
    test_cases = ["Abc123!@", "Abcdef12!", "Abc123!@@", "AAAAb12!@"]
    for pwd in test_cases:
        result = is_valid_password(pwd)
        print(result)