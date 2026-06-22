import unicodedata
import string

class PasswordValidator:
    UNICODE_MIN = 0
    UNICODE_MAX = 0x10FFFF
    SURROGATE_MIN = 0xD800
    SURROGATE_MAX = 0xDFFF
    LOWER_CHARS = string.ascii_lowercase
    UPPER_CHARS = string.ascii_uppercase
    DIGIT_CHARS = string.digits

    def __init__(self, password: str):
        self.password = password
        self._is_unicode_valid = self._validate_unicode_codepoints()
        self._class_count = 0
        self._class_names = []
        if self._is_unicode_valid:
            self._class_count = self._count_character_classes()

    def _validate_unicode_codepoints(self) -> bool:
        if not isinstance(self.password, str):
            return False
        if len(self.password) == 0:
            return False
        for char in self.password:
            code_point = ord(char)
            if code_point < self.UNICODE_MIN or code_point > self.UNICODE_MAX:
                return False
            if self.SURROGATE_MIN <= code_point <= self.SURROGATE_MAX:
                return False
        return True

    def _count_character_classes(self) -> int:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for char in self.password:
            if char in self.LOWER_CHARS:
                has_lower = True
            elif char in self.UPPER_CHARS:
                has_upper = True
            elif char in self.DIGIT_CHARS:
                has_digit = True
            elif not char.isspace():
                cat = unicodedata.category(char)
                if cat.startswith('P') or cat.startswith('S') or cat.startswith('Sm'):
                    has_special = True

            if has_lower and has_upper and has_digit and has_special:
                break

        count = 0
        if has_lower:
            count += 1
        if has_upper:
            count += 1
        if has_digit:
            count += 1
        if has_special:
            count += 1
        return count

    def is_valid(self) -> bool:
        if not self._is_unicode_valid:
            return False
        return self._class_count >= 3

    def get_details(self) -> dict:
        return {
            "valid": self.is_valid(),
            "class_count": self._class_count,
            "unicode_valid": self._is_unicode_valid
        }

if __name__ == '__main__':
    test_passwords = [
        "SecurePass123",
        "weak",
        "AllUnicodeValid™️#1",
        "1234567890",
        "MixedCaseNoDigits",
        "Valid$Pass7"
    ]

    for pwd in test_passwords:
        validator = PasswordValidator(pwd)
        result = validator.get_details()
        print(f"Password: {pwd}, Valid: {result['valid']}, Classes: {result['class_count']}")