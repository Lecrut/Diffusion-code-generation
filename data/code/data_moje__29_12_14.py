VOWELS_LOWER = "aeiou"
VOWELS_UPPER = "AEIOU"
ALL_VOWELS = frozenset(VOWELS_LOWER + VOWELS_UPPER)

def count_vowels(text: str) -> int:
    return sum(1 for char in text if char in ALL_VOWELS)

if __name__ == '__main__':
    sample_phrase = "The quick brown fox jumps over the lazy dog"
    total_count = count_vowels(sample_phrase)
    print(total_count)