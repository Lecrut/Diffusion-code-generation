import string

SPECIAL_CHARS = set(string.punctuation)

def contains_special_chars(s):
    return bool(set(s) & SPECIAL_CHARS)

if __name__ == '__main__':
    sample_strings = ["Hello World!", "NoSpecialsHere", "Test@123#"]
    for text in sample_strings:
        print(contains_special_chars(text))