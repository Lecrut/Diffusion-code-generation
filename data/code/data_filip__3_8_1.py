import re

def strip_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = strip_vowels(sample_text)
    print(result)