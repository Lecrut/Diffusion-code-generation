import re
import string

class PasswordValidator:
    _SPECIAL_CHARS = set(string.punctuation)
    _KEYBOARD_ROWS = [
        "1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./"
    ]

    @staticmethod
    def _has_min_length(password, min_length=12):
        return len(password) >= min_length

    @staticmethod
    def _has_two_different_special_chars(password):
        specials_in_password = [c for c in password if c in PasswordValidator._SPECIAL_CHARS]
        unique_specials = set(specials_in_password)
        return len(unique_specials) >= 2

    @staticmethod
    def _has_sequential_keyboard_pattern(password, window_size=3):
        lower_password = password.lower()
        for row in PasswordValidator._KEYBOARD_ROWS:
            for i in range(len(row) - window_size + 1):
                substring = row[i:i + window_size]
                if substring in lower_password:
                    return True
            for i in range(len(row) - window_size + 1):
                substring = row[i:i + window_size][::-1]
                if substring in lower_password:
                    return True
        return False

    @staticmethod
    def validate(password):
        if not PasswordValidator._has_min_length(password):
            return False
        if not PasswordValidator._has_two_different_special_chars(password):
            return False
        if PasswordValidator._has_sequential_keyboard_pattern(password):
            return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    samples = [
        "StrongP@ss#word1",
        "short!",
        "NoSpecialChars123",
        "HasSpecials!@#12345",
        "qwe!@#12345678",
        "ValidPassw0rd!@"
    ]
    for sample in samples:
        result = validator.validate(sample)
        print(f"{sample}: {result}")