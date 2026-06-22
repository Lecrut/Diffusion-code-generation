import re
import string

class PasswordValidator:
    @staticmethod
    def is_valid(password):
        if len(password) < 12:
            return False

        special_chars = set(string.punctuation)
        found_specials = [c for c in password if c in special_chars]
        unique_specials = set(found_specials)
        if len(unique_specials) < 2:
            return False

        if PasswordValidator._has_sequential_pattern(password):
            return False

        return True

    @staticmethod
    def _has_sequential_pattern(password):
        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        
        lower_pwd = password.lower()
        
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                forward_seq = row[i:i+3]
                backward_seq = forward_seq[::-1]
                if forward_seq in lower_pwd or backward_seq in lower_pwd:
                    return True
                    
        for i in range(len(lower_pwd) - 2):
            three_chars = lower_pwd[i:i+3]
            if three_chars == three_chars[::-1]:
                continue
            chars = list(three_chars)
            codes = [ord(c) for c in chars]
            if codes[1] - codes[0] == 1 and codes[2] - codes[1] == 1:
                return True
            if codes[0] - codes[1] == 1 and codes[1] - codes[2] == 1:
                return True
                
        return False

if __name__ == '__main__':
    validator = PasswordValidator()
    test_cases = [
        "short!@",
        "LongEnough1!",
        "ValidP@ssw0rd!",
        "qwertyuiop12",
        "Strong&P@ss12",
        "Abcd321!@#",
        "12345678!@#$",
        "NoSpecialChars12",
        "OnlyOneSpecial123!",
        "ComplexP@ss&12"
    ]
    
    for pwd in test_cases:
        result = validator.is_valid(pwd)
        print(f"{pwd}: {result}")