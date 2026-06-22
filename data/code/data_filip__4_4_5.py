VOWELS = set('aeiouAEIOU')

def count_consonants(text: str) -> int:
    total_chars = len(text)
    vowel_count = sum(1 for char in text if char in VOWELS)
    non_alpha_count = sum(1 for char in text if not char.isalpha())
    consonant_count = total_chars - vowel_count - non_alpha_count
    return consonant_count

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = count_consonants(sample_text)
    print(result)