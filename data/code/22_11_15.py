import re

def validate_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+\[\]{}|;:\'",.<>?/\\`~])[A-Za-z\d!@#$%^&*()\-_=+\[\]{}|;:\'",.<>?/\\`~]{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    test_passwords = [
        "Short1!",
        "nopass",
        "AllLowercase1!",
        "NODIGITSHERE!",
        "NoSpecial1",
        "ValidP@ssw0rd"
    ]
    for p in test_passwords:
        print(validate_password(p))