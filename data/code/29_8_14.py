import re
import string

VOWEL_PATTERN = r'[aeiouAEIOU]'
TEST_TEXT = "The quick brown fox jumps over the lazy dog"

def count_vowel_occurrences(input_text):
    occurrences = re.findall(VOWEL_PATTERN, input_text)
    return len(occurrences)

if __name__ == '__main__':
    computed_count = count_vowel_occurrences(TEST_TEXT)
    print(computed_count)