import re

_special_char_pattern = re.compile(r"[^a-zA-Z0-9\s]")

def contains_special_characters(text):
    return bool(_special_char_pattern.search(text))

if __name__ == '__main__':
    test_strings = ["HelloWorld", "Hello@World", "12345", "Test#Case", "  spaced  "]
    for s in test_strings:
        print(contains_special_characters(s))