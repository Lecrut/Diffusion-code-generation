import string

VOWELS = 'aeiouAEIOU'
VOWEL_COUNT_TABLE = str.maketrans('', '', VOWELS)

def count_vowels(text: str) -> int:
    stripped = text.translate(VOWEL_COUNT_TABLE)
    return len(text) - len(stripped)

if __name__ == '__main__':
    sample_text = "This is a sample string with various vowels: A, E, I, O, U, and their lowercase counterparts. Also, special chars!@# are ignored."
    result = count_vowels(sample_text)
    print(result)