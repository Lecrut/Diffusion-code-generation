import re

_special_char_regex = re.compile(r'[^a-zA-Z0-9\s]')

def has_special_characters(text):
    return bool(_special_char_regex.search(text))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello@World!",
        "12345",
        "Test string with special chars: @#$%",
        "NoSpecialChars123",
        " ",
        "a!b@c#d"
    ]
    for s in sample_strings:
        print(has_special_characters(s))