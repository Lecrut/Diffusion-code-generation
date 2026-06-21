import re
import itertools

class PasswordValidator:
    def __init__(self):
        self.min_length = 12
        self.special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
        self.keyboard_rows = [
            "1234567890-=",
            "qwertyuiop[]\\" ,
            "asdfghjkl;'",
            "zxcvbnm,./"
        ]

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False

        special_count = sum(1 for c in password if c in "!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
        if special_count < 2:
            return False

        if PasswordValidator._has_sequential_pattern(password):
            return False

        return True

    @staticmethod
    def _has_sequential_pattern(password):
        keyboard_rows = [
            "1234567890-=",
            "qwertyuiop[]\\",
            "asdfghjkl;'",
            "zxcvbnm,./"
        ]

        password_lower = password.lower()
        pattern_len = 3

        for row in keyboard_rows:
            row_lower = row.lower()
            for i in range(len(row_lower) - pattern_len + 1):
                seq = row_lower[i:i+pattern_len]
                if seq in password_lower:
                    return True
                rev_seq = seq[::-1]
                if rev_seq in password_lower:
                    return True

        return False

if __name__ == '__main__':
    validator = PasswordValidator()
    print(validator.validate("Abcdefghijkl"))
    print(validator.validate("Abcdef!@ghijk"))
    print(validator.validate("Abcdef!@ghijkl"))
    print(validator.validate("Pass!@word123"))
    print(validator.validate("qwe!@#1234567"))