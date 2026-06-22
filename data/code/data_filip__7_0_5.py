import re

SPECIAL_CHAR_PATTERN = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text: str) -> bool:
    return bool(SPECIAL_CHAR_PATTERN.search(text))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello@World",
        "12345",
        "NoSpecialCharsHere123",
        "Special!@#$%^&*()Characters"
    ]

    for s in sample_strings:
        result = contains_special_characters(s)
        print(result)