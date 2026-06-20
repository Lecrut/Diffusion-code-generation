import re

def has_special_chars(text: str) -> bool:
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello@World",
        "Test#123",
        "NoSpecialHere123",
        "!@#$%"
    ]
    for s in sample_strings:
        print(has_special_chars(s))