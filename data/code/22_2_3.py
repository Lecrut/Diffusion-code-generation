class PasswordValidator:
    @staticmethod
    def is_sequential_char(char1, char2):
        return abs(ord(char1) - ord(char2)) == 1

    @staticmethod
    def has_sequential_pattern(password):
        i = 0
        while i < len(password) - 1:
            c1 = password[i]
            c2 = password[i + 1]
            if c1.isalpha() and c2.isalpha():
                if c1.lower() == c2.lower() or PasswordValidator.is_sequential_char(c1, c2):
                    return True
            elif c1.isdigit() and c2.isdigit():
                if PasswordValidator.is_sequential_char(c1, c2):
                    return True
            i += 1
        return False

    @staticmethod
    def validate_password_complexity(password):
        if len(password) < 12:
            return False
        special_chars = set("!@#$%^&*()_+-=[]{}|;:,.<>?/`~")
        found_special = 0
        unique_special = set()
        for char in password:
            if char in special_chars:
                found_special += 1
                unique_special.add(char)
                if len(unique_special) >= 2:
                    break
        if found_special < 2:
            return False
        if PasswordValidator.has_sequential_pattern(password):
            return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    valid_password = "Str0ng!Pass@Word"
    result = validator.validate_password_complexity(valid_password)
    print(result)