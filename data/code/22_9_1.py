import unicodedata
import string

class UnicodePasswordValidator:
    VALID_UNICODE_RANGE = (0, 0x10FFFF)
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF

    def __init__(self, password):
        self.password = password
        self.is_unicode_valid = self._verify_unicode_integrity()

    def _verify_unicode_integrity(self):
        for char in self.password:
            code_point = ord(char)
            if code_point < self.VALID_UNICODE_RANGE[0] or code_point > self.VALID_UNICODE_RANGE[1]:
                return False
            if self.SURROGATE_START <= code_point <= self.SURROGATE_END:
                return False
        return True

    def _get_char_categories(self):
        categories = set()
        for char in self.password:
            if char.isupper():
                categories.add('upper')
            if char.islower():
                categories.add('lower')
            if char.isdigit():
                categories.add('digit')
            if not char.isalnum() and unicodedata.category(char).startswith('S') or unicodedata.category(char).startswith('P') or unicodedata.category(char) in ('Cs', 'Co', 'Cn', 'Cc', 'Cf', 'Zl', 'Zp', 'Zs'):
                categories.add('special')
        return categories

    def validate(self):
        if not self.is_unicode_valid:
            return False
        categories = self._get_char_categories()
        return len(categories) >= 3

if __name__ == '__main__':
    validator1 = UnicodePasswordValidator("P@ssw0rd")
    print(validator1.validate())

    validator2 = UnicodePasswordValidator("hello")
    print(validator2.validate())

    validator3 = UnicodePasswordValidator("A1b!")
    print(validator3.validate())

    validator4 = UnicodePasswordValidator("\ud800")
    print(validator4.validate())