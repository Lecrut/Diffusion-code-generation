import re

def strip_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_input = "Hello World"
    result = strip_vowels(sample_input)
    print(result)