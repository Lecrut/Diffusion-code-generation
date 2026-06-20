import re

def has_special_chars(text):
    if not isinstance(text, str):
        return False
    pattern = r'[^a-zA-Z0-9\s]'
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    sample_values = ["Hello World", "Test@123", "NoSpecialCharsHere", "Special!Char", "   spaced   "]
    for value in sample_values:
        result = has_special_chars(value)
        print(f"{value!r}: {result}")