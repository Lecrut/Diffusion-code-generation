import unicodedata

class PasswordValidator:
    def __init__(self):
        self.classes = ["upper", "lower", "digit", "symbol"]

    def _has_upper(self, pwd):
        for char in pwd:
            if unicodedata.category(char).startswith('Lu'):
                return True
        return False

    def _has_lower(self, pwd):
        for char in pwd:
            if unicodedata.category(char).startswith('Ll'):
                return True
        return False

    def _has_digit(self, pwd):
        for char in pwd:
            if unicodedata.category(char).startswith('Nd'):
                return True
        return False

    def _has_symbol(self, pwd):
        for char in pwd:
            cat = unicodedata.category(char)
            if cat.startswith('P') or cat.startswith('S') or cat.startswith('Z'):
                return True
        return False

    def validate(self, password):
        if not password:
            return False
        
        has_unicode = False
        for char in password:
            if ord(char) > 127:
                has_unicode = True
                break
        
        if not has_unicode:
            return False

        found_classes = 0
        if self._has_upper(password):
            found_classes += 1
        if self._has_lower(password):
            found_classes += 1
        if self._has_digit(password):
            found_classes += 1
        if self._has_symbol(password):
            found_classes += 1

        return found_classes >= 3

if __name__ == '__main__':
    validator = PasswordValidator()
    test_pwd = "Привет1!@#"
    result = validator.validate(test_pwd)
    print(result)
    test_pwd2 = "HelloWorld123"
    result2 = validator.validate(test_pwd2)
    print(result2)