VOWELS = set("aeiouAEIOU")

def count_consonants(text: str) -> int:
    total_chars = len(text)
    vowel_count = sum(1 for char in text if char in VOWELS)
    alpha_count = sum(1 for char in text if char.isalpha())
    consonant_count = alpha_count - vowel_count
    return consonant_count

if __name__ == "__main__":
    sample_text = "Hello World!"
    result = count_consonants(sample_text)
    print(result)