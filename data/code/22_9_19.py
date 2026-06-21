class PasswordValidator:
    UNICODE_MAX = 0x10FFFF
    SURROGATE_START = 0xD800
    SURROGATE_END = 0xDFFF

    def __init__(self, password):
        self.password = password

    def is_unicode_valid(self):
        if not isinstance(self.password, str):
            return False
        for char in self.password:
            code_point = ord(char)
            if code_point < 0 or code_point > self.UNICODE_MAX:
                return False
            if self.SURROGATE_START <= code_point <= self.SURROGATE_END:
                return False
        return True

    def get_character_classes_count(self):
        if not self.is_unicode_valid():
            return 0

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in self.password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if not char.isalnum():
                has_symbol = True

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

    def is_valid(self):
        return self.is_unicode_valid() and self.get_character_classes_count() >= 3

if __name__ == '__main__':
    validator1 = PasswordValidator("HelloWorld123!")
    print(validator1.is_valid())

    validator2 = PasswordValidator("hello123")
    print(validator2.is_valid())

    validator3 = PasswordValidator("ABCdef")
    print(validator3.is_valid())

    validator4 = PasswordValidator("Pass 123")
    print(validator4.is_valid())

    validator5 = PasswordValidator("")
    print(validator5.is_valid())