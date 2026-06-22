import sys

VOWELS = set('aeiouAEIOU')

def build_translation_map():
    mapping = {chr(i): 0 for i in range(sys.maxunicode + 1)}
    for char in VOWELS:
        mapping[char] = 1
    return mapping

TRANSLATION_MAP = build_translation_map()

def count_vowels_optimized(text):
    total = 0
    for char in text:
        total += TRANSLATION_MAP.get(char, 0)
    return total

if __name__ == '__main__':
    sample_text = "A quick brown fox jumps over the lazy dog. The 5000 apples were eaten by 12 people. AEIOUaeiou!"
    result = count_vowels_optimized(sample_text)
    print(result)