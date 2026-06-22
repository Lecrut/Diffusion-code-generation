import re

class PasswordValidator:
    def __init__(self, min_length=8, max_repeating=3):
        self.min_length = min_length
        self.max_repeating = max_repeating

    def has_repeating_chars(self, password):
        if len(password) < self.max_repeating + 1:
            return False
        for i in range(len(password) - self.max_repeating):
            segment = password[i:i + self.max_repeating + 1]
            if len(set(segment)) == 1:
                return True
        return False

    def validate(self, password):
        if not isinstance(password, str):
            return False
        if len(password) < self.min_length:
            return False
        if self.has_repeating_chars(password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    sample_passwords = [
        "Weak1!",
        "StrongP@ss1",
        "aaaaB1!",
        "ValidP@ss1word!",
        "NoSpecialChars1",
        "12345678",
        "ABCDEF1!",
        "validP@ss1"
    ]
    for pwd in sample_passwords:
        print(validator.validate(pwd))