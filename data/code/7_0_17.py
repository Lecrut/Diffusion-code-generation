import re

_special_char_pattern = re.compile(r'[^A-Za-z0-9\s]')

def contains_special_chars(text: str) -> bool:
    return bool(_special_char_pattern.search(text))

if __name__ == '__main__':
    print(contains_special_chars("Hello, World!"))
    print(contains_special_chars("HelloWorld"))
    print(contains_special_chars("12345"))
    print(contains_special_chars("NoSpecialCharsHere"))