import re

VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text):
    return VOWEL_PATTERN.sub('', text)

if __name__ == '__main__':
    sample_input = "Programming is fun and efficient"
    result = remove_vowels(sample_input)
    print(result)