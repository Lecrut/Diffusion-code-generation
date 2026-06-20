import string
import re

def find_first_special(text: str):
    if not text:
        return None
    
    special_chars = set(string.punctuation)
    
    for char in text:
        if char in special_chars:
            return char
    
    return None

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello@World",
        "Test123!",
        "NoSpecialCharsHere",
        "",
        "!First",
        "Last@Symbol"
    ]
    
    for s in sample_strings:
        result = find_first_special(s)
        print(result)