import re

VOWELS_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return VOWELS_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)