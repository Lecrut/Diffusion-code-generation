def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string, case-insensitive.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [
        "Hello, World!",           # Expected: 2 (e, o)
        "AEIOU",                   # Expected: 5
        "rhythm",                  # Expected: 0
        "aeiouaeiou",              # Expected: 8
        "",                        # Expected: 0
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"Input: '{sample}' -> Vowel Count: {result}")