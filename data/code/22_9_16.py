import unicodedata
import re

class PasswordValidator:
    VALID_MAX = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF
    MIN_CLASSES = 3

    def __init__(self, password: str):
        self.password = password
        self.is_valid = self._run_validation()

    def _run_validation(self) -> bool:
        if not self._check_unicode_support():
            return False
        return self._check_character_classes() >= self.MIN_CLASSES

    def _check_unicode_support(self) -> bool:
        for char in self.password:
            code = ord(char)
            if code > self.VALID_MAX:
                return False
            if self.SURROGATE_START <= code <= self.SURROGATE_END:
                return False
        return True

    def _check_character_classes(self) -> int:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for char in self.password:
            if not has_lower:
                if char.islower():
                    has_lower = True
            if not has_upper:
                if char.isupper():
                    has_upper = True
            if not has_digit:
                if char.isdigit():
                    has_digit = True
            if not has_special:
                if not char.isalnum():
                    has_special = True
            if has_lower and has_upper and has_digit and has_special:
                return 4

        return sum([has_lower, has_upper, has_digit, has_special])

if __name__ == '__main__':
    samples = [
        "Short",
        "123456",
        "P@ssw0rd!",
        "abcdef",
        "Abc!123",
        "NoSpecial123",
        "NoDigits!abc",
        "NOLOWERCASE123!",
        "ALLGOOD123!",
        "üñíçödéP@ss1",
        "\uD800",
        "Valid_Unicode_123!",
        "JustLetters",
        "123Numbers",
        "SymbolsOnly!!!",
        "A1!b",
    ]

    for sample in samples:
        validator = PasswordValidator(sample)
        print(f"Password: {repr(sample)}, Valid: {validator.is_valid}")