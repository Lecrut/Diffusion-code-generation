import re

def strip_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU aeiou",
        "No Vowels Here",
        ""
    ]
    for s in sample_strings:
        print(strip_vowels(s))