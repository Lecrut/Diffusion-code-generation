import re

_special_chars_re = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text):
    return bool(_special_chars_re.search(text))

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "hello@world",
        "plain123",
        "special#char",
        "   ",
        ""
    ]
    for s in sample_strings:
        print(contains_special_characters(s))