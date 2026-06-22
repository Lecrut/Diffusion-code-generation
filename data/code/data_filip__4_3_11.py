ALPHABET_VOWELS = frozenset("aeiouAEIOU")

def is_vowel(char):
    return char in ALPHABET_VOWELS

def count_consonants(text):
    if not isinstance(text, str):
        return 0
    if len(text) == 0:
        return 0
    consonant_chars = [char for char in text if char.isalpha() and not is_vowel(char)]
    return len(consonant_chars)

if __name__ == '__main__':
    sample_data = "The quick brown fox jumps over the lazy dog 12345!"
    calculated_result = count_consonants(sample_data)
    print(calculated_result)