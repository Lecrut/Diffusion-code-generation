class PasswordValidator:
    @staticmethod
    def validate(password: str) -> bool:
        if len(password) < 12:
            return False

        special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
        found_specials = [char for char in password if char in special_chars]
        if len(set(found_specials)) < 2:
            return False

        keyboard_rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
            "1234567890",
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        for row in keyboard_rows:
            for i in range(len(password) - 1):
                char1 = password[i].lower()
                char2 = password[i + 1].lower()
                if char1 in row and char2 in row:
                    idx1 = row.index(char1)
                    idx2 = row.index(char2)
                    if idx2 == idx1 + 1:
                        return False
                    if idx1 == idx2 + 1:
                        return False

        return True

if __name__ == '__main__':
    validator = PasswordValidator()
    print(validator.validate("Aa1!bC@2dE#3"))
    print(validator.validate("short!@"))
    print(validator.validate("abcdefg!@"))