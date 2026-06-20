import string
import re

SPECIAL_SYMBOLS = set(string.punctuation)

def contains_special_chars(text: str) -> bool:
    text_set = set(text)
    intersection = text_set.intersection(SPECIAL_SYMBOLS)
    return bool(intersection)

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = contains_special_chars(sample_string)
    print(result)