VOWELS = frozenset("aeiouAEIOU")

def count_consonants(s: str) -> int:
    total = len(s)
    vowel_count = sum(1 for char in s if char in VOWELS)
    non_alpha_count = sum(1 for char in s if not char.isalpha())
    return total - vowel_count - non_alpha_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_consonants(sample_string)
    print(result)