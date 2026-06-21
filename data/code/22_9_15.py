import re
import unicodedata

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password
        self._unicode_valid = self._check_unicode()
        self._class_count = 0
        if self._unicode_valid:
            self._class_count = self._count_classes()

    def _check_unicode(self) -> bool:
        if not isinstance(self.password, str):
            return False
        for char in self.password:
            code_point = ord(char)
            if 0xD800 <= code_point <= 0xDFFF:
                return False
            if code_point > 0x10FFFF:
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
                else:
                    has_upper = True
            elif char.isdigit():
                has_digit = True
            elif unicodedata.category(char).startswith('P') or unicodedata.category(char).startswith('S') or unicodedata.category(char).startswith('Z'):
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

    def is_strong(self) -> bool:
        return self._unicode_valid and self._class_count >= 3

if __name__ == '__main__':
    validator = PasswordValidator("Abc123!@#€")
    print(validator.is_strong())
    print(validator._class_count)
    print(validator._unicode_valid)

    weak_validator = PasswordValidator("abc")
    print(weak_validator.is_strong())
    print(weak_validator._class_count)

    emoji_validator = PasswordValidator("Pass1234🎉")
    print(emoji_validator.is_strong())
    print(emoji_validator._class_count)
    print(emoji_validator._unicode_valid)

    invalid_unicode_validator = PasswordValidator("Pass\u0000D")
    print(invalid_unicode_validator.is_strong())
    print(invalid_unicode_validator._class_count)
    print(invalid_unicode_validator._unicode_valid)

    empty_validator = PasswordValidator("")
    print(empty_validator.is_strong())
    print(empty_validator._class_count)
    print(empty_validator._unicode_valid)

    special_only_validator = PasswordValidator("!@#$%^&*")
    print(special_only_validator.is_strong())
    print(special_only_validator._class_count)
    print(special_only_validator._unicode_valid)

    mixed_unicode_validator = PasswordValidator("Пароль1234")
    print(mixed_unicode_validator.is_strong())
    print(mixed_unicode_validator._class_count)
    print(mixed_unicode_validator._unicode_valid)

    class_validator = PasswordValidator("aA1!")
    print(class_validator.is_strong())
    print(class_validator._class_count)
    print(class_validator._unicode_valid)

    unicode_class_validator = PasswordValidator("Пароль1!")
    print(unicode_class_validator.is_strong())
    print(unicode_class_validator._class_count)
    print(unicode_class_validator._unicode_valid)

    invalid_type_validator = PasswordValidator(12345)
    print(invalid_type_validator.is_strong())
    print(invalid_type_validator._class_count)
    print(invalid_type_validator._unicode_valid)

    surrogate_validator = PasswordValidator("Pass\uD800D")
    print(surrogate_validator.is_strong())
    print(surrogate_validator._class_count)
    print(surrogate_validator._unicode_valid)

    valid_unicode_class_validator = PasswordValidator("Пароль!1")
    print(valid_unicode_class_validator.is_strong())
    print(valid_unicode_class_validator._class_count)
    print(valid_unicode_class_validator._unicode_valid)

    mixed_valid_unicode_class_validator = PasswordValidator("Пароль!@#A1")
    print(mixed_valid_unicode_class_validator.is_strong())
    print(mixed_valid_unicode_class_validator._class_count)
    print(mixed_valid_unicode_class_validator._unicode_valid)

    complex_unicode_validator = PasswordValidator("Привет123!@#")
    print(complex_unicode_validator.is_strong())
    print(complex_unicode_validator._class_count)
    print(complex_unicode_validator._unicode_valid)

    minimal_strong_validator = PasswordValidator("aA1@")
    print(minimal_strong_validator.is_strong())
    print(minimal_strong_validator._class_count)
    print(minimal_strong_validator._unicode_valid)

    minimal_weak_validator = PasswordValidator("aaA1")
    print(minimal_weak_validator.is_strong())
    print(minimal_weak_validator._class_count)
    print(minimal_weak_validator._unicode_valid)

    special_unicode_validator = PasswordValidator("Пароль@#$%")
    print(special_unicode_validator.is_strong())
    print(special_unicode_validator._class_count)
    print(special_unicode_validator._unicode_valid)

    emoji_special_validator = PasswordValidator("Pass!@#🎉")
    print(emoji_special_validator.is_strong())
    print(emoji_special_validator._class_count)
    print(emoji_special_validator._unicode_valid)

    long_unicode_validator = PasswordValidator("aA1bB2cC3dD4eE5fF6gG7hH8iI9jJ0kK1lL2mM3nN4oO5pP6qQ7rR8sS9tT0uU1vV2wW3xX4yY5zZ6!")
    print(long_unicode_validator.is_strong())
    print(long_unicode_validator._class_count)
    print(long_unicode_validator._unicode_valid)

    short_unicode_validator = PasswordValidator("a")
    print(short_unicode_validator.is_strong())
    print(short_unicode_validator._class_count)
    print(short_unicode_validator._unicode_valid)

    short_strong_validator = PasswordValidator("aA1@")
    print(short_strong_validator.is_strong())
    print(short_strong_validator._class_count)
    print(short_strong_validator._unicode_valid)

    short_weak_validator = PasswordValidator("a")
    print(short_weak_validator.is_strong())
    print(short_weak_validator._class_count)
    print(short_weak_validator._unicode_valid)

    short_special_validator = PasswordValidator("!")
    print(short_special_validator.is_strong())
    print(short_special_validator._class_count)
    print(short_special_validator._unicode_valid)

    short_digit_validator = PasswordValidator("1")
    print(short_digit_validator.is_strong())
    print(short_digit_validator._class_count)
    print(short_digit_validator._unicode_valid)

    short_upper_validator = PasswordValidator("A")
    print(short_upper_validator.is_strong())
    print(short_upper_validator._class_count)
    print(short_upper_validator._unicode_valid)

    short_lower_validator = PasswordValidator("a")
    print(short_lower_validator.is_strong())
    print(short_lower_validator._class_count)
    print(short_lower_validator._unicode_valid)

    short_lower_digit_validator = PasswordValidator("a1")
    print(short_lower_digit_validator.is_strong())
    print(short_lower_digit_validator._class_count)
    print(short_lower_digit_validator._unicode_valid)

    short_lower_upper_validator = PasswordValidator("aA")
    print(short_lower_upper_validator.is_strong())
    print(short_lower_upper_validator._class_count)
    print(short_lower_upper_validator._unicode_valid)

    short_lower_special_validator = PasswordValidator("a@")
    print(short_lower_special_validator.is_strong())
    print(short_lower_special_validator._class_count)
    print(short_lower_special_validator._unicode_valid)

    short_upper_digit_validator = PasswordValidator("A1")
    print(short_upper_digit_validator.is_strong())
    print(short_upper_digit_validator._class_count)
    print(short_upper_digit_validator._unicode_valid)

    short_upper_special_validator = PasswordValidator("A@")
    print(short_upper_special_validator.is_strong())
    print(short_upper_special_validator._class_count)
    print(short_upper_special_validator._unicode_valid)

    short_digit_special_validator = PasswordValidator("1@")
    print(short_digit_special_validator.is_strong())
    print(short_digit_special_validator._class_count)
    print(short_digit_special_validator._unicode_valid)

    short_lower_upper_digit_validator = PasswordValidator("aA1")
    print(short_lower_upper_digit_validator.is_strong())
    print(short_lower_upper_digit_validator._class_count)
    print(short_lower_upper_digit_validator._unicode_valid)

    short_lower_upper_special_validator = PasswordValidator("aA@")
    print(short_lower_upper_special_validator.is_strong())
    print(short_lower_upper_special_validator._class_count)
    print(short_lower_upper_special_validator._unicode_valid)

    short_lower_digit_special_validator = PasswordValidator("a1@")
    print(short_lower_digit_special_validator.is_strong())
    print(short_lower_digit_special_validator._class_count)
    print(short_lower_digit_special_validator._unicode_valid)

    short_upper_digit_special_validator = PasswordValidator("A1@")
    print(short_upper_digit_special_validator.is_strong())
    print(short_upper_digit_special_validator._class_count)
    print(short_upper_digit_special_validator._unicode_valid)

    short_lower_upper_digit_special_validator = PasswordValidator("aA1@")
    print(short_lower_upper_digit_special_validator.is_strong())
    print(short_lower_upper_digit_special_validator._class_count)
    print(short_lower_upper_digit_special_validator._unicode_valid)