class PasswordValidator:
    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False
        special_chars = set()
        for char in password:
            if not char.isalnum():
                special_chars.add(char)
        if len(special_chars) < 2:
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
            "1234567890"
        ]
        lower_pass = password.lower()
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                forward = row[i:i+3]
                backward = forward[::-1]
                if forward in lower_pass or backward in lower_pass:
                    return True
        return False

if __name__ == '__main__':
    print(PasswordValidator.validate("abc123!@"))
    print(PasswordValidator.validate("StrongP@ssw0rd!!"))
    print(PasswordValidator.validate("qwe123!@#$"))
    print(PasswordValidator.validate("MyV3ryStr0ng!Pass#"))
    print(PasswordValidator.validate("Short!@#"))
    print(PasswordValidator.validate("NoSpecialChar123456"))