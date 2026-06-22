import re

def has_special_characters(s: str) -> bool:
    pattern = r'[^a-zA-Z0-9\s]'
    return bool(re.search(pattern, s))

if __name__ == '__main__':
    sample_strings = [
        "HelloWorld",
        "Hello World!",
        "NoSpecial123",
        "Has@Special#Char"
    ]

    for s in sample_strings:
        result = has_special_characters(s)
        print(result)