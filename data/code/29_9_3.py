import string

VOWELS = set('aeiouAEIOU')
VOWEL_COUNT_TABLE = str.maketrans('', '', string.ascii_lowercase + string.ascii_uppercase)
VOWEL_ONLY_TABLE = str.maketrans(''.join(c for c in string.ascii_lowercase + string.ascii_uppercase if c in VOWELS), '')

def count_vowels(text: str) -> int:
    if not text:
        return 0
    vowels_text = text.translate(VOWEL_ONLY_TABLE)
    return len(vowels_text)

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string with some vowels like a, e, i, o, u. And uppercase A, E, I, O, U."
    result = count_vowels(sample_text)
    print(result)