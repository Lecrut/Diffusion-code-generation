import re

VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

def remove_vowels(input_string):
    cleaned_text = VOWEL_PATTERN.sub('', input_string)
    return cleaned_text

if __name__ == '__main__':
    test_phrase = "Remove all vowels from this string"
    final_output = remove_vowels(test_phrase)
    print(final_output)