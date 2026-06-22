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
    test_passwords = [
        "short1!",
        "nouppercase1!",
        "nolowercase1!",
        "nodigit!",
        "nospecial1",
        "ValidPass1!",
        "AnotherValid1@",
        "12345678",
        "abcdefgh",
        "ABCDEFGH",
        "Abcdefgh",
        "Abcdefg1",
        "Abcdefg!",
        "Abcdefg1!"
    ]
    results = [validate_password_strength(p) for p in test_passwords]
    print(list(zip(test_passwords, results)))