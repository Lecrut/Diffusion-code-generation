import unicodedata
import re

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password
        self._unicode_valid = self._check_unicode()
        self._class_count = 0
        if self._unicode_valid:
            self._class_count = self._count_classes()

    def _check_unicode(self) -> bool:
        if not isinstance(self.password, str):
            return False
        for char in self.password:
            code_point = ord(char)
            if 0xD800 <= code_point <= 0xDFFF:
                return False
            if code_point > 0x10FFFF:
                return False
        return True

    def _is_digit(self, char: str) -> bool:
        return char.isdigit()

    def _is_upper(self, char: str) -> bool:
        return char.isupper()

    def _is_lower(self, char: str) -> bool:
        return char.islower()

    def _is_symbol(self, char: str) -> bool:
        cat = unicodedata.category(char)
        return not (cat.startswith('L') or cat.startswith('N') or cat.startswith('C') or cat.startswith('Z'))

    def _count_classes(self) -> int:
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False
        for char in self.password:
            if not has_upper and self._is_upper(char):
                has_upper = True
            if not has_lower and self._is_lower(char):
                has_lower = True
            if not has_digit and self._is_digit(char):
                has_digit = True
            if not has_symbol and self._is_symbol(char):
                has_symbol = True
        count = sum([has_upper, has_lower, has_digit, has_symbol])
        return count

    def is_valid(self) -> bool:
        if not self._unicode_valid:
            return False
        return self._class_count >= 3

SAMPLE_PASSWORD_STRONG = "Str0ng!Pass"
SAMPLE_PASSWORD_WEAK = "weak"
SAMPLE_PASSWORD_NO_UNICODE = "Valid!Pass1"

def main():
    validator_strong = PasswordValidator(SAMPLE_PASSWORD_STRONG)
    result_strong = validator_strong.is_valid()
    print(result_strong)
    
    validator_weak = PasswordValidator(SAMPLE_PASSWORD_WEAK)
    result_weak = validator_weak.is_valid()
    print(result_weak)
    
    validator_unicode = PasswordValidator(SAMPLE_PASSWORD_NO_UNICODE)
    result_unicode = validator_unicode.is_valid()
    print(result_unicode)

if __name__ == '__main__':
    main()