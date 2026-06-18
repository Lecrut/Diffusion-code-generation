def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in a string case-insensitively."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test sentence with many vowels: aeioou."
    result = count_vowels(sample_string)
    print(f"Total number of vowels found: {result}")