import re

_special_char_regex = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text):
    return bool(_special_char_regex.search(text))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello World!",
        "NoSpecial123",
        "Has@Symbol",
        "Spaces   and   tabs\t",
        "Mixed: 123 & letters!",
        ""
    ]
    for s in sample_strings:
        result = contains_special_characters(s)
        print(f"contains_special_characters({repr(s)}) = {result}")