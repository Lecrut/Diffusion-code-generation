class PasswordValidator:
    @staticmethod
    def validate_password(password):
        if len(password) < 12:
            return False
        
        special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
        found_specials = [c for c in password if c in special_chars]
        if len(set(found_specials)) < 2:
            return False
        
        if PasswordValidator._has_sequential_pattern(password):
            return False
        
        return True
    
    @staticmethod
    def _has_sequential_pattern(password):
        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "1234567890",
            "!@#$%^&*()",
            "_-+=[]{}\\|",
            ";:',.<>?"
        ]
        
        password_lower = password.lower()
        
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                sequence_forward = row[i:i+3]
                sequence_backward = row[i:i+3][::-1]
                if sequence_forward in password_lower or sequence_backward in password_lower:
                    return True
        
        return False

if __name__ == '__main__':
    validator = PasswordValidator()
    
    test_passwords = [
        "abc!@#123456",
        "SecureP@ss123!!",
        "hello!world@123",
        "qwerty123!!",
        "a!b@c#d$e%12345",
        "short!@#",
        "noSpecialChar123456",
        "ValidP@ssw0rd!!"
    ]
    
    results = []
    for pwd in test_passwords:
        is_valid = PasswordValidator.validate_password(pwd)
        results.append((pwd, is_valid))
    
    for pwd, valid in results:
        print(f"{pwd}: {valid}")