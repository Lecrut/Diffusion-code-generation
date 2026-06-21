import unicodedata

VALID_UNICODE_MAX = 0x10FFFF
SURROGATE_START = 0xD800
SURROGATE_END = 0xDFFF

class PasswordVerifier:
    def __init__(self, text):
        self.text = text
        self._unicode_ok = self._verify_unicode()
        self._class_count = self._count_classes() if self._unicode_ok else 0

    def _verify_unicode(self):
        for char in self.text:
            cp = ord(char)
            if cp > VALID_UNICODE_MAX:
                return False
            if SURROGATE_START <= cp <= SURROGATE_END:
                return False
        return True

    def _count_classes(self):
        found_upper = False
        found_lower = False
        found_digit = False
        found_special = False

        for char in self.text:
            cat = unicodedata.category(char)
            if cat.startswith('Lu') and not found_upper:
                found_upper = True
            elif cat.startswith('Ll') and not found_lower:
                found_lower = True
            elif cat.startswith('Nd') and not found_digit:
                found_digit = True
            elif not cat.startswith(('L', 'N', 'Z')) and not found_special:
                found_special = True

        if found_upper and found_lower and found_digit and found_special:
            return 4
        return sum([found_upper, found_lower, found_digit, found_special])

    def is_valid(self):
        return self._class_count >= 3

if __name__ == '__main__':
    sample1 = PasswordVerifier("StrongP@ss1")
    print(sample1.is_valid())
    sample2 = PasswordVerifier("weak")
    print(sample2.is_valid())
    sample3 = PasswordVerifier("12345678")
    print(sample3.is_valid())
    sample4 = PasswordVerifier("Abcdefgh")
    print(sample4.is_valid())
    sample5 = PasswordVerifier("!@#$%^&*")
    print(sample5.is_valid())
    sample6 = PasswordVerifier("P@ssword")
    print(sample6.is_valid())