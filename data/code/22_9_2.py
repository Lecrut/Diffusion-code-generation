import unicodedata
import string

class PasswordStrengthChecker:
    UNICODE_MIN = 0
    UNICODE_MAX = 0x10FFFF
    SURROGATE_MIN = 0xD800
    SURROGATE_MAX = 0xDFFF
    ASCII_UPPER = string.ascii_uppercase
    ASCII_LOWER = string.ascii_lowercase
    ASCII_DIGITS = string.digits

    def __init__(self, password):
        self.password = password
        self._unicode_valid = self._validate_unicode_range()
        self._class_count = self._calculate_class_count() if self._unicode_valid else 0

    def _validate_unicode_range(self):
        for char in self.password:
            code = ord(char)
            if code < self.UNICODE_MIN or code > self.UNICODE_MAX:
                return False
            if self.SURROGATE_MIN <= code <= self.SURROGATE_MAX:
                return False
        return True

    def _is_ascii_upper(self, char):
        return char in self.ASCII_UPPER

    def _is_ascii_lower(self, char):
        return char in self.ASCII_LOWER

    def _is_digit(self, char):
        return char in self.ASCII_DIGITS

    def _is_symbol(self, char):
        if not self._is_ascii_upper(char) and not self._is_ascii_lower(char) and not self._is_digit(char):
            return True
        return False

    def _calculate_class_count(self):
        flags = [False, False, False, False]
        for char in self.password:
            if not flags[0] and self._is_ascii_upper(char):
                flags[0] = True
            elif not flags[1] and self._is_ascii_lower(char):
                flags[1] = True
            elif not flags[2] and self._is_digit(char):
                flags[2] = True
            elif not flags[3] and self._is_symbol(char):
                flags[3] = True
            if all(flags):
                break
        return sum(flags)

    def is_valid(self):
        if not self._unicode_valid:
            return False
        return self._class_count >= 3

    def get_details(self):
        return self._unicode_valid, self._class_count, self.password

if __name__ == '__main__':
    test_cases = [
        "HelloWorld123",
        "abc123",
        "UPPER!@#lower99",
        "Caf\u00e9Strong#1",
        "\ud800bad"
    ]
    
    for sample in test_cases:
        checker = PasswordStrengthChecker(sample)
        result, count, original = checker.get_details()
        print(f"Password: {original} | Unicode Valid: {result} | Classes Found: {count} | Is Strong: {checker.is_valid()}")