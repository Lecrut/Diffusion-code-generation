import re

def filter_vowels(text):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string with AEIOU and aeiou."
    result = filter_vowels(sample_text)
    print(result)