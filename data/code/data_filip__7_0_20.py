import re

_SPECIAL_CHARS_PATTERN = re.compile(r'[^\w\s]')

def has_special_characters(text: str) -> bool:
    return bool(_SPECIAL_CHARS_PATTERN.search(text))

if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Hello@World!"
    result_1 = has_special_characters(test_string_1)
    result_2 = has_special_characters(test_string_2)
    print(result_1)
    print(result_2)