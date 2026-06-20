import string
import re

def contains_special_characters(text):
    special_chars = set(string.punctuation)
    pattern = re.compile(f"[{re.escape(''.join(special_chars))}]")
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample1 = "Hello World!"
    sample2 = "NoSpecialsHere"
    sample3 = "Test@123"
    print(contains_special_characters(sample1))
    print(contains_special_characters(sample2))
    print(contains_special_characters(sample3))