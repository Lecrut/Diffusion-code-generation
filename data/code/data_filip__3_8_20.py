import re

def strip_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    result = strip_vowels(sample_string)
    print(result)