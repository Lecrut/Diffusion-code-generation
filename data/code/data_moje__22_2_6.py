import re
import string

class PasswordValidator:
    KEYBOARD_ROWS = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "1234567890"
    ]

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        
        if not PasswordValidator._has_two_distinct_special_chars(password):
            return False
        
        if PasswordValidator._has_sequential_pattern(password):
            return False
        
        return True

    @staticmethod
    def _has_two_distinct_special_chars(password):
        special_chars = set()
        for char in password:
            if not char.isalnum():
                special_chars.add(char)
                if len(special_chars) >= 2:
                    return True
        return False

    @staticmethod
    def _has_sequential_pattern(password):
        lower_pwd = password.lower()
        for row in PasswordValidator.KEYBOARD_ROWS:
            for i in range(len(row) - 2):
                seq = row[i : i + 3]
                if seq in lower_pwd:
                    return True
        return False

if __name__ == '__main__':
    sample_passwords = [
        "SecurePass123!",
        "WeakPass1!",
        "GoodPass123!@#",
        "qwer1234AbCd!@"
    ]
    
    results = []
    for pwd in sample_passwords:
        result = PasswordValidator.validate(pwd)
        results.append(f"{pwd}: {result}")
    
    print(results)