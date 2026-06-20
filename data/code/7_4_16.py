import string
import re

def find_first_special(s: str) -> str | None:
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    sample_strings = [
        "HelloWorld",
        "Hello_World!",
        "12345",
        "Test#Case",
        "",
        "Normal text without specials"
    ]
    for text in sample_strings:
        result = find_first_special(text)
        print(result)