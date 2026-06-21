import unicodedata
import string

class PasswordValidator:
    UNICODE_MAX = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF
    ASCII_DIGITS = string.digits
    ASCII_LOWERCASE = string.ascii_lowercase
    ASCII_UPPERCASE = string.ascii_uppercase
    SPECIAL_CHARS = set(string.punctuation)

    def __init__(self, password: str):
        self.password = password
        self._is_unicode_valid = self._verify_unicode()
        self._class_count = 0
        if self._is_unicode_valid:
            self._class_count = self._count_character_classes()

    def _verify_unicode(self) -> bool:
        if not isinstance(self.password, str):
            return False
        for char in self.password:
            code_point = ord(char)
            if code_point > self.UNICODE_MAX:
                return False
            if self.SURROGATE_START <= code_point <= self.SURROGATE_END:
                return False
        return True

    def _count_character_classes(self) -> int:
        flags = {
            'digit': False,
            'lower': False,
            'upper': False,
            'special': False
        }
        
        for char in self.password:
            if char in self.ASCII_DIGITS:
                flags['digit'] = True
            elif char in self.ASCII_LOWERCASE:
                flags['lower'] = True
            elif char in self.ASCII_UPPERCASE:
                flags['upper'] = True
            elif char in self.SPECIAL_CHARS:
                flags['special'] = True
            elif unicodedata.category(char).startswith('L'):
                flags['lower'] = True
            elif unicodedata.category(char).startswith('Nd'):
                flags['digit'] = True
        
        return sum(flags.values())

    def is_valid(self) -> bool:
        if not self._is_unicode_valid:
            return False
        return self._class_count >= 3

    def get_class_count(self) -> int:
        return self._class_count

    def is_unicode_valid(self) -> bool:
        return self._is_unicode_valid

if __name__ == '__main__':
    sample_passwords = [
        "SecurePass123!",
        "weak",
        "Mix3dChars#",
        "InvalidSurrogate\uDBFF\uDC00",
        "Привет123!",
        "12345678",
        "ALLUPPERCASE1"
    ]
    
    for pwd in sample_passwords:
        validator = PasswordValidator(pwd)
        print(f"Password: {pwd!r} | Valid: {validator.is_valid()} | Classes: {validator.get_class_count()} | UnicodeOK: {validator.is_unicode_valid()}")