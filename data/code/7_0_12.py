import re

_special_char_pattern = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text):
    return bool(_special_char_pattern.search(text))

if __name__ == '__main__':
    print(contains_special_characters("Hello World"))
    print(contains_special_characters("Hello@World"))
    print(contains_special_characters("12345"))
    print(contains_special_characters("Test!@#$%"))
    print(contains_special_characters(""))
    print(contains_special_characters("   "))