VOWELS = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})

def count_consonants(text: str) -> int:
    total_length = len(text)
    vowel_count = sum(1 for char in text if char in VOWELS)
    non_alpha_count = sum(1 for char in text if not char.isalpha())
    return total_length - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)