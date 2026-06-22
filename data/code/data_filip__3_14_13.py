import re

_VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return _VOWEL_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    result = remove_vowels(sample_text)
    print(result)