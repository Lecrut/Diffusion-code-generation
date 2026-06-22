import re
import string

class PasswordValidator:
    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            return False

        if len(password) < 12:
            return False

        special_chars = set(string.punctuation)
        found_specials = [c for c in password if c in special_chars]
        if len(set(found_specials)) < 2:
            return False

        if PasswordValidator._has_sequential_patterns(password):
            return False

        return True

    @staticmethod
    def _has_sequential_patterns(password):
        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "1234567890"
        ]
        
        password_lower = password.lower()
        
        for row in keyboard_rows:
            for length in range(3, len(row) + 1):
                for start in range(len(row) - length + 1):
                    forward_seq = row[start:start+length]
                    backward_seq = forward_seq[::-1]
                    if forward_seq in password_lower or backward_seq in password_lower:
                        return True
                        
        number_seq = "0123456789"
        for length in range(3, len(number_seq) + 1):
            for start in range(len(number_seq) - length + 1):
                forward_seq = number_seq[start:start+length]
                backward_seq = forward_seq[::-1]
                if forward_seq in password_lower or backward_seq in password_lower:
                    return True
                    
        alpha_seq = "abcdefghijklmnopqrstuvwxyz"
        for length in range(3, len(alpha_seq) + 1):
            for start in range(len(alpha_seq) - length + 1):
                forward_seq = alpha_seq[start:start+length]
                backward_seq = forward_seq[::-1]
                if forward_seq in password_lower or backward_seq in password_lower:
                    return True

        return False

if __name__ == '__main__':
    validator = PasswordValidator()
    
    test_passwords = [
        "Short!@#",
        "LongEnough!@#",
        "NoSpecial12345678",
        "TwoSpec@l!Chars123",
        "qwert123!@#",
        "321rewq!@#",
        "abc123!@#",
        "321cba!@#",
        "ValidPwd!@#9xyz",
        "P@ssw0rd!@#123"
    ]
    
    for pwd in test_passwords:
        result = validator.validate_password(pwd)
        print(f"{pwd}: {result}")