import re
import unicodedata

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password

    def check_unicode_support(self) -> bool:
        for char in self.password:
            code_point = ord(char)
            if code_point > 0x10FFFF:
                return False
            if 0xD800 <= code_point <= 0xDFFF:
                return False
        return True

    def count_character_classes(self) -> int:
        classes_count = 0
        for char in self.password:
            if unicodedata.category(char).startswith('L'):
                classes_count |= 1
            elif unicodedata.category(char).startswith('N'):
                classes_count |= 2
            elif unicodedata.category(char).startswith('S'):
                classes_count |= 4
            elif unicodedata.category(char).startswith('P'):
                classes_count |= 8
            if classes_count == 15:
                break
        return bin(classes_count).count('1')

    def validate(self) -> dict:
        unicode_supported = self.check_unicode_support()
        classes_count = self.count_character_classes()
        is_valid = unicode_supported and classes_count >= 3
        return {
            "valid": is_valid,
            "unicode_supported": unicode_supported,
            "classes_count": classes_count,
            "password_length": len(self.password)
        }

if __name__ == '__main__':
    validator = PasswordValidator("MyP@ssw0rd_123")
    result = validator.validate()
    print(result)