import re

def filter_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample = "Hello World"
    result = filter_vowels(sample)
    print(result)