import unicodedata

class PasswordSecurityChecker:
    VALID_CP_MAX = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF
    MIN_CLASSES = 3

    def __init__(self, secret: str):
        self.secret = secret

    def _is_unicode_safe(self) -> bool:
        for char in self.secret:
            cp = ord(char)
            if cp > self.VALID_CP_MAX:
                return False
            if self.SURROGATE_START <= cp <= self.SURROGATE_END:
                return False
        return True

    def _detect_classes(self) -> int:
        categories = unicodedata.category
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in self.secret:
            cat = categories(char)
            if cat.startswith('Lu'):
                has_upper = True
            elif cat.startswith('Ll'):
                has_lower = True
            elif cat.startswith('Nd'):
                has_digit = True
            elif cat.startswith('S') or cat.startswith('P'):
                has_symbol = True
            
            if has_upper and has_lower and has_digit and has_symbol:
                return 4
        
        count = 0
        if has_upper:
            count += 1
        if has_lower:
            count += 1
        if has_digit:
            count += 1
        if has_symbol:
            count += 1
            
        return count

    def verify(self) -> bool:
        if not self._is_unicode_safe():
            return False
        classes_found = self._detect_classes()
        return classes_found >= self.MIN_CLASSES

if __name__ == '__main__':
    samples = [
        "Abc123!",
        "password",
        "ABC123",
        "a1b2c3!@#",
        "Hello World 123",
        "P@ssw0rd",
        "simple",
        "C0mpl3x!ty",
    ]

    results = []
    for sample in samples:
        checker = PasswordSecurityChecker(sample)
        results.append((sample, checker.verify()))

    for password, is_valid in results:
        print(password, is_valid)