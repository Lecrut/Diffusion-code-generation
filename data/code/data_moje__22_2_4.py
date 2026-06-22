class PasswordValidator:
    SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
    KEYPAD_PATTERNS = [
        "qwertyuiop", "asdfghjkl", "zxcvbnm",
        "1234567890", "0987654321",
        "!@#$%^&*()", "qazwsx", "wsxedc", "xcvfrt", "rfvtgb", "tgbyhn", "yhnujm",
        "qwert", "asdf", "zxcv", "1234", "9876"
    ]

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        special_count = 0
        seen_specials = set()
        for char in password:
            if char in PasswordValidator.SPECIAL_CHARS:
                seen_specials.add(char)
        if len(seen_specials) < 2:
            return False
        lower_pwd = password.lower()
        for i in range(len(lower_pwd) - 3):
            substring = lower_pwd[i : i + 4]
            if any(substring in pattern for pattern in PasswordValidator.KEYPAD_PATTERNS):
                return False
            rev_substring = substring[::-1]
            if any(rev_substring in pattern for pattern in PasswordValidator.KEYPAD_PATTERNS):
                return False
        return True

if __name__ == '__main__':
    sample_valid = "StrongPass!@123"
    sample_invalid_short = "Short!@1"
    sample_invalid_one_special = "OneSpecialChar#123456"
    sample_invalid_pattern = "qwerty123456!@"
    print(PasswordValidator.validate(sample_valid))
    print(PasswordValidator.validate(sample_invalid_short))
    print(PasswordValidator.validate(sample_invalid_one_special))
    print(PasswordValidator.validate(sample_invalid_pattern))