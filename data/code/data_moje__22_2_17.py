import re

class PasswordValidator:
    SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{}|;:,.<>?/`~")

    @staticmethod
    def is_sequential_pattern(password):
        if len(password) < 3:
            return False
        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"
        ]
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                substring = row[i : i + 3]
                if substring in password or substring[::-1] in password:
                    return True
        return False

    @staticmethod
    def validate(password):
        if not isinstance(password, str):
            return False
        if len(password) < 12:
            return False
        special_chars_found = set()
        for char in password:
            if char in PasswordValidator.SPECIAL_CHARS:
                special_chars_found.add(char)
                if len(special_chars_found) >= 2:
                    break
        if len(special_chars_found) < 2:
            return False
        if PasswordValidator.is_sequential_pattern(password):
            return False
        return True

if __name__ == '__main__':
    sample_passwords = [
        "SecurePass123!",
        "MyStr0ng#Pass$wd",
        "qwerty123456!@",
        "Abcdefghijkl#$",
        "ValidP@ss#1234"
    ]
    for pwd in sample_passwords:
        result = PasswordValidator.validate(pwd)
        print(f"{pwd}: {result}")