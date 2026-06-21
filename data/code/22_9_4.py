import unicodedata
import string

class PasswordValidator:
    UNICODE_MAX = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF
    MIN_CLASSES = 3

    def __init__(self, password):
        self.password = password
        self._unicode_valid = self._check_unicode_support()
        self._class_count = 0
        if self._unicode_valid:
            self._class_count = self._count_character_classes()

    def _check_unicode_support(self):
        for char in self.password:
            code_point = ord(char)
            if code_point > self.UNICODE_MAX:
                return False
            if self.SURROGATE_START <= code_point <= self.SURROGATE_END:
                return False
        return True

    def _is_upper(self, char):
        cat = unicodedata.category(char)
        return cat.startswith('Lu')

    def _is_lower(self, char):
        cat = unicodedata.category(char)
        return cat.startswith('Ll')

    def _is_digit(self, char):
        cat = unicodedata.category(char)
        return cat.startswith('Nd')

    def _is_special(self, char):
        return not self._is_upper(char) and not self._is_lower(char) and not self._is_digit(char)

    def _count_character_classes(self):
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for char in self.password:
            if self._is_upper(char):
                has_upper = True
            if self._is_lower(char):
                has_lower = True
            if self._is_digit(char):
                has_digit = True
            if self._is_special(char):
                has_special = True

        count = 0
        if has_upper:
            count += 1
        if has_lower:
            count += 1
        if has_digit:
            count += 1
        if has_special:
            count += 1

        return count

    def is_valid(self):
        return self._unicode_valid and self._class_count >= self.MIN_CLASSES

    def get_unicode_status(self):
        return self._unicode_valid

    def get_class_count(self):
        return self._class_count

if __name__ == '__main__':
    samples = [
        "Password1!",
        "short",
        "12345678",
        "ABCDEF123456!",
        "\U0001F600Test1!",
        "NoSpecials123",
        "noUpper123!",
        "NoDigitsABC!",
        "Specials!!!",
        "A1!"
    ]
    for sample in samples:
        validator = PasswordValidator(sample)
        print(validator.is_valid())