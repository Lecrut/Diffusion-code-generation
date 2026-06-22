import unicodedata

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password
        self._unicode_valid = self._verify_unicode()
        self._class_count = self._count_classes() if self._unicode_valid else 0

    def _verify_unicode(self) -> bool:
        for char in self.password:
            code_point = ord(char)
            if 0xD800 <= code_point <= 0xDFFF:
                return False
            if code_point > 0x10FFFF:
                return False
        return True

    def _count_classes(self) -> int:
        classes_count = 0
        for char in self.password:
            category = unicodedata.category(char)
            if category.startswith('L'):
                classes_count |= 1
            elif category.startswith('N') and not category.startswith('No'):
                classes_count |= 2
            elif category.startswith('S'):
                classes_count |= 4
            elif char in string.punctuation:
                classes_count |= 4
        return bin(classes_count).count('1')

import string

def is_valid(password: str) -> bool:
    validator = PasswordValidator(password)
    return validator._unicode_valid and validator._class_count >= 3

if __name__ == '__main__':
    sample_password = "Røld@123"
    result = is_valid(sample_password)
    print(result)