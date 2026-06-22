import re

_VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return _VOWEL_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = remove_vowels(sample_input)
    print(result)