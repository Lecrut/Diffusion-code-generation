class PasswordValidator:
    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        special_count = 0
        special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/")
        for char in password:
            if char in special_chars:
                special_count += 1
        if special_count < 2:
            return False
        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "1234567890",
            "!@#$%^&*()",
        ]
        lower_password = password.lower()
        for row in keyboard_rows:
            reversed_row = row[::-1]
            for i in range(len(lower_password) - 2):
                sub = lower_password[i:i+3]
                if sub in row or sub in reversed_row:
                    return False
        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    print(validator.validate("Tr0ub4dor&3!"))
    print(validator.validate("abc!@#$%^&*"))
    print(validator.validate("abcdefghijkl"))