import re
import string

class PasswordValidator:

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False

        special_chars = set(string.punctuation)
        found_specials = [c for c in password if c in special_chars]
        if len(set(found_specials)) < 2:
            return False

        keyboard_patterns = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "0987654321",
            "1234567890",
            "qwert",
            "asdfg",
            "zxcvb",
            "12345",
            "54321"
        ]

        lower_password = password.lower()
        for pattern in keyboard_patterns:
            for i in range(len(lower_password) - len(pattern) + 1):
                if lower_password[i:i + len(pattern)] == pattern:
                    return False

        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    result = validator.validate("Abcdefghijkl!@#")
    print(result)