import re

def strip_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample = "Hello World"
    result = strip_vowels(sample)
    print(result)