def count_vowels(text: str) -> int:
    """Count vowels in a string, handling both uppercase and lowercase letters."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    sample_1 = "Hello World"
    sample_2 = "AEIOU AEIOU"
    
    result_1 = count_vowels(sample_1)
    result_2 = count_vowels(sample_2)
    
    print(f"Vowel count in '{sample_1}': {result_1}")
    print(f"Vowel count in '{sample_2}': {result_2}")