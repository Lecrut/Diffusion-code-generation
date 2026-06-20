import re

VOWEL_PATTERN = r'[aeiouAEIOU]'

def strip_vowels(text):
    return re.sub(VOWEL_PATTERN, '', text)

if __name__ == '__main__':
    test_input = "Remove all vowels"
    output = strip_vowels(test_input)
    print(output)