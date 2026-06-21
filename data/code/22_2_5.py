class PasswordValidator:
    @staticmethod
    def is_complex(password):
        if len(password) < 12:
            return False
        
        special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/`~")
        found_specials = set()
        has_upper = False
        has_lower = False
        has_digit = False
        
        for char in password:
            if char in special_chars:
                found_specials.add(char)
            elif char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
        
        if len(found_specials) < 2:
            return False
        if not (has_upper and has_lower and has_digit):
            return False
        
        if PasswordValidator._has_sequential_pattern(password):
            return False
            
        return True

    @staticmethod
    def _has_sequential_pattern(password):
        lower_password = password.lower()
        sequential_keys = [
            "abcdefghijklmnopqrstuvwxyz",
            "0123456789",
            "!@#$%^&*()",
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        
        for seq in sequential_keys:
            for i in range(len(seq) - 2):
                triad = seq[i:i+3]
                rev_trid = triad[::-1]
                if triad in lower_password or rev_trid in lower_password:
                    return True
        return False

if __name__ == '__main__':
    validator = PasswordValidator()
    result1 = validator.is_complex("Str0ng!#Pass")
    print(result1)
    result2 = validator.is_complex("Abcdefghijk")
    print(result2)
    result3 = validator.is_complex("Pass@Word!1234567890")
    print(result3)