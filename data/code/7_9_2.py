import string
import re

def has_special_characters(s: str) -> bool:
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return True
    return False

if __name__ == '__main__':
    test_string_1 = "Hello World!"
    test_string_2 = "JustLetters"
    test_string_3 = "1234567890"
    test_string_4 = "Special@#Characters"

    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))
    print(has_special_characters(test_string_3))
    print(has_special_characters(test_string_4))