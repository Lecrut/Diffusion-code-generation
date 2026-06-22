class PasswordValidator:
    MIN_LENGTH = 12
    REQUIRED_SPECIAL_COUNT = 2
    KEYBOARD_ROWS = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "1234567890",
        "!@#$%^&*()"
    ]

    @staticmethod
    def _has_sequential_pattern(password):
        lower_pwd = password.lower()
        for row in PasswordValidator.KEYBOARD_ROWS:
            for i in range(len(row) - 2):
                seq = row[i : i + 3]
                if seq in lower_pwd:
                    return True
                if seq[::-1] in lower_pwd:
                    return True
        for i in range(len(password) - 2):
            c1, c2, c3 = password[i], password[i+1], password[i+2]
            if c1.isalpha() and c2.isalpha() and c3.isalpha():
                if c1.isupper() == c2.isupper() == c3.isupper():
                    o1, o2, o3 = ord(c1.lower()), ord(c2.lower()), ord(c3.lower())
                    if o2 - o1 == 1 and o3 - o2 == 1:
                        return True
            elif c1.isdigit() and c2.isdigit() and c3.isdigit():
                v1, v2, v3 = int(c1), int(c2), int(c3)
                if v2 - v1 == 1 and v3 - v2 == 1:
                    return True
                if v1 - v2 == 1 and v2 - v3 == 1:
                    return True
        return False

    @staticmethod
    def _count_unique_specials(password):
        special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/")
        found = set()
        for char in password:
            if char in special_chars:
                found.add(char)
        return len(found)

    @staticmethod
    def validate(password):
        if len(password) < PasswordValidator.MIN_LENGTH:
            return False
        if PasswordValidator._count_unique_specials(password) < PasswordValidator.REQUIRED_SPECIAL_COUNT:
            return False
        if PasswordValidator._has_sequential_pattern(password):
            return False
        return True

if __name__ == '__main__':
    test_cases = [
        "Short!@#",
        "ValidPassword123!@",
        "qwertyasdfgh123!@",
        "AaBbCcDdEeFf!@#$",
        "ComplexPass!@##123",
        "Sequential!@qwer123",
        "StrongPassword!!12"
    ]
    for case in test_cases:
        result = PasswordValidator.validate(case)
        print(f"Password: {case} -> Valid: {result}")