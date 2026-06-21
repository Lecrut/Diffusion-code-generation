import unicodedata

class PasswordValidationEngine:
    def __init__(self, password):
        self.password = password

    def validate_unicode_support(self):
        for char in self.password:
            code_point = ord(char)
            if code_point < 0 or code_point > 0x10FFFF:
                return False
            if 0xD800 <= code_point <= 0xDFFF:
                return False
        return True

    def count_satisfied_classes(self):
        if not self.validate_unicode_support():
            return 0

        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special = False

        for char in self.password:
            if not has_uppercase and char.isupper():
                has_uppercase = True
            if not has_lowercase and char.islower():
                has_lowercase = True
            if not has_digit and char.isdigit():
                has_digit = True
            if not has_special and not char.isalnum():
                has_special = True

        count = sum([has_uppercase, has_lowercase, has_digit, has_special])
        return count

    def is_valid(self):
        satisfied_classes = self.count_satisfied_classes()
        return satisfied_classes >= 3

if __name__ == '__main__':
    test_pass_1 = "Str0ng!Pass"
    test_pass_2 = "weak"
    test_pass_3 = "12345678"
    test_pass_4 = "ABCDEF"
    test_pass_5 = "!@#$%^&*"
    test_pass_6 = "ValidP@ss1"

    validator_1 = PasswordValidationEngine(test_pass_1)
    print(validator_1.is_valid())

    validator_2 = PasswordValidationEngine(test_pass_2)
    print(validator_2.is_valid())

    validator_3 = PasswordValidationEngine(test_pass_3)
    print(validator_3.is_valid())

    validator_4 = PasswordValidationEngine(test_pass_4)
    print(validator_4.is_valid())

    validator_5 = PasswordValidationEngine(test_pass_5)
    print(validator_5.is_valid())

    validator_6 = PasswordValidationEngine(test_pass_6)
    print(validator_6.is_valid())