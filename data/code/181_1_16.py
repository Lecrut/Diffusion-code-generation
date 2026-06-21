import re

VOWEL_PATTERN = r'[aeiou]'

def find_vowels_in_words(texts):
    vowels_set = set()
    for text in texts:
        matches = re.findall(VOWEL_PATTERN, text.lower())
        vowels_set.update(matches)
    return list(vowels_set)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Rhythm"
    sample4 = "Programming is Fun"
    samples = [sample1, sample2, sample3, sample4]
    result = find_vowels_in_words(samples)
    print(f"Vowels in provided texts: {result}")