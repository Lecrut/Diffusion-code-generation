class PasswordValidator:
    @staticmethod
    def validate(password: str) -> bool:
        if len(password) < 12:
            return False

        special_count = 0
        special_chars = set("!@#$%^&*()-_=+[]{}|;:,.<>?/~`")
        for char in password:
            if char in special_chars:
                special_count += 1
        if special_count < 2:
            return False

        sequential_patterns = [
            "abcdefghijklmnopqrstuvwxyz",
            "zyxwvutsrqponmlkjihgfedcba",
            "0123456789",
            "9876543210",
            "qwertyuiop",
            "poiuytrewq",
            "asdfghjkl",
            "lkjhgfdsa",
            "zxcvbnm",
            "mnbvcxz",
            "QWERTYUIOP",
            "POIUYTREWQ",
            "ASDFGHJKL",
            "LKJHGFDSA",
            "ZXCVBNM",
            "MNBVCXZ",
            "!@#$%^&*()",
            ")(*&^%$#!@"
        ]

        lower_password = password.lower()
        for pattern in sequential_patterns:
            for i in range(len(lower_password) - 2):
                segment = lower_password[i:i+3]
                if segment in pattern:
                    return False

        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    valid_password = "Str0ng!P@ss#"
    invalid_password = "Weak1!"
    weak_sequential = "Abcd1234abcd!"
    
    print(validator.validate(valid_password))
    print(validator.validate(invalid_password))
    print(validator.validate(weak_sequential))