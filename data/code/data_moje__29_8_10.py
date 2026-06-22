import re

VALIDATION_ERROR = "Input must be a string"
VOWEL_PATTERN = r'[aeiouAEIOU]'

def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError(VALIDATION_ERROR)
    matches = re.findall(VOWEL_PATTERN, text)
    return len(matches)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    vowel_count = count_vowels(sample_text)
    print(vowel_count)