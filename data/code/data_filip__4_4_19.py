VOWELS = frozenset("aeiouAEIOU")

TEXT = "The quick brown fox jumps over the lazy dog"

def count_consonants(text, vowels):
    length = len(text)
    vowel_count = 0
    non_alpha_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif not char.isalpha():
            non_alpha_count += 1
    consonant_count = length - vowel_count - non_alpha_count
    return consonant_count

if __name__ == '__main__':
    result = count_consonants(TEXT, VOWELS)
    print(result)