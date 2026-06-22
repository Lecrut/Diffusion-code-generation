import re

SPECIAL_CHAR_PATTERN = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_characters(text):
    if SPECIAL_CHAR_PATTERN.search(text):
        return True
    return False

if __name__ == '__main__':
    test_strings = ["Hello World", "Hello@World", "Python3.9", "Safe123", "NoSpecialCharsHere"]
    for s in test_strings:
        print(contains_special_characters(s))