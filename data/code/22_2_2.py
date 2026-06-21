import re
import string

class PasswordValidator:
    keyboard_sequences = [
        "qwertyuiop", "asdfghjkl", "zxcvbnm",
        "1234567890", "!@#$%^&*()",
        "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM",
        "0987654321", ")(*&^%$#@!",
        "qwerty", "asdfgh", "zxcvbn",
        "123456", "!@#$%^"
    ]

    @staticmethod
    def validate(password):
        if len(password) < 12:
            return False

        special_chars = set(string.punctuation)
        found_specials = [c for c in password if c in special_chars]
        unique_specials = set(found_specials)
        if len(unique_specials) < 2:
            return False

        lower_password = password.lower()
        for seq in PasswordValidator.keyboard_sequences:
            if seq in lower_password:
                return False

        return True

if __name__ == '__main__':
    test_passwords = [
        "Abcdefghijkl",
        "A1!@#Bcdefghij",
        "Password123",
        "Tr0ub4dor&3",
        "MyStr0ng!@Pass",
        "qwertyuiop12",
        "A!B#CcDdEeFf",
        "123456789012",
        "Hello@World!1",
        "Ab3!@Cd5#Fg7Hi"
    ]
    results = [PasswordValidator.validate(p) for p in test_passwords]
    print(results)