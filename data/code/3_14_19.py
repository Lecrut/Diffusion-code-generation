import re

VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]', re.UNICODE)

def remove_vowels(text: str) -> str:
    return VOWEL_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)