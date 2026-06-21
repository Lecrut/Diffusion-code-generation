import unicodedata
import string

class PasswordValidator:
    MAX_CODE_POINT = 0x10FFFF
    SURROGATE_LOW = 0xD800
    SURROGATE_HIGH = 0xDFFF
    MIN_CLASSES = 3

    def __init__(self, password: str):
        self.password = password
        self._unicode_valid = self._validate_unicode()
        self._class_count = 0
        if self._unicode_valid:
            self._class_count = self._count_classes()

    def _validate_unicode(self) -> bool:
        if not isinstance(self.password, str):
            return False
        for char in self.password:
            code_point = ord(char)
            if code_point > self.MAX_CODE_POINT:
                return False
            if self.SURROGATE_LOW <= code_point <= self.SURROGATE_HIGH:
                return False
        return True

    def _count_classes(self) -> int:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        for char in self.password:
            if unicodedata.category(char).startswith('L'):
                if char.islower():
                    has_lower = True
                elif char.isupper():
                    has_upper = True
            elif char.isdecimal():
                has_digit = True
            elif char in string.punctuation:
                has_special = True
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
        return self._unicode_valid and self._class_count >= self.MIN_CLASSES

    def get_class_count(self) -> int:
        return self._class_count

if __name__ == '__main__':
    validator = PasswordValidator("MyP@ssw0rd")
    result = validator.is_valid()
    class_count = validator.get_class_count()
    print(f"{result} with {class_count} classes")
    weak_validator = PasswordValidator("weakpass")
    weak_result = weak_validator.is_valid()
    print(weak_result)
    unicode_validator = PasswordValidator("Password123!@#")
    unicode_result = unicode_validator.is_valid()
    print(unicode_result)