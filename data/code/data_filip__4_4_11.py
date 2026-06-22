VOWELS = frozenset("aeiouAEIOU")

def count_consonants(text: str) -> int:
    vowel_count = sum(1 for char in text if char in VOWELS)
    non_alpha_count = sum(1 for char in text if not char.isalpha())
    total_length = len(text)
    return total_length - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)