import re

VOWEL_PATTERN = r'[aeiouAEIOU]'

def strip_vowels(text: str) -> str:
    return re.sub(VOWEL_PATTERN, '', text)

if __name__ == '__main__':
    test_cases = [
        "Programming is fun",
        "A quick brown fox",
        "The quick brown fox jumps over the lazy dog",
        "AEIOUaeiou",
        "rhythm"
    ]
    for case in test_cases:
        print(strip_vowels(case))