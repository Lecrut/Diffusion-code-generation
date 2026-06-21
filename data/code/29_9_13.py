import sys

VOWELS = 'aeiouAEIOU'
TRANSLATION_MAP = {ord(c): None for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for c in VOWELS:
    del TRANSLATION_MAP[ord(c)]

def count_vowels_optimized(text: str) -> int:
    non_vowel_text = text.translate(TRANSLATION_MAP)
    return len(text) - len(non_vowel_text)

if __name__ == '__main__':
    large_sample = "The quick brown fox jumps over the lazy dog." * 50000
    final_count = count_vowels_optimized(large_sample)
    print(final_count)