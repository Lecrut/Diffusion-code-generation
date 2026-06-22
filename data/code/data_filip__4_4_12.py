VOWELS = set("aeiouAEIOU")

TEXT = "The quick brown fox jumps over the lazy dog"

def count_consonants(text):
    total_length = len(text)
    vowel_count = sum(1 for char in text if char in VOWELS)
    non_alpha_count = sum(1 for char in text if not char.isalpha())
    consonant_count = total_length - vowel_count - non_alpha_count
    return consonant_count

if __name__ == '__main__':
    result = count_consonants(TEXT)
    print(result)