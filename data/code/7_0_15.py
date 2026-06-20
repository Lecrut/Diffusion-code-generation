import re

SPECIAL_CHAR_PATTERN = re.compile(r'[^a-zA-Z0-9\s]')

def contains_special_chars(text):
    return bool(SPECIAL_CHAR_PATTERN.search(text))

if __name__ == '__main__':
    sample_1 = "Hello World"
    sample_2 = "Hello@World!"
    sample_3 = "NoSpecialCharsHere123"
    sample_4 = "Special#123"
    
    print(contains_special_chars(sample_1))
    print(contains_special_chars(sample_2))
    print(contains_special_chars(sample_3))
    print(contains_special_chars(sample_4))