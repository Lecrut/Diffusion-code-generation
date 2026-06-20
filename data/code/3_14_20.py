import re

VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return VOWEL_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_input = "Hello World, welcome to Python programming!"
    result = remove_vowels(sample_input)
    print(result)