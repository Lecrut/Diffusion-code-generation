import re

def filter_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test String with vowels."
    result = filter_vowels(sample_text)
    print(result)