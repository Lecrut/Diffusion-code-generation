import re

def validate_password(password):
    pattern = r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    test_passwords = [
        "Short1!",
        "NoDigitA!",
        "NoUppercase1!",
        "NoSpecial1a",
        "Valid1!",
        "Valid1234!",
        "aBcD1234!",
        "Ab1!AaAa"
    ]
    for pw in test_passwords:
        result = validate_password(pw)
        print(result)