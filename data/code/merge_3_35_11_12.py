def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in the input string.
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [
        "Hello, World!",      # Expected: 3 (e, o, o)
        "aeiouAEIOU",         # Expected: 10
        "",                   # Expected: 0
        "Python Programming!",# Expected: 4 (y is not counted here based on strict aeiou definition)
        "Rhythm"              # Expected: 2 (i, o - wait, R-y-t-h-m. No vowels? Actually 'o' in rhythm? No. r-y-t-h-m. Correct count is 0 for standard dict vowel set if y excluded.)
    ]

    print("Testing optimized count_vowels function:")
    for i, sample_text in enumerate(samples, 1):
        result = count_vowels(sample_text)
        # Note on "Rhythm": r-y-t-h-m has no a,e,i,o,u. Count is 0.
        # Previous thought about 'o' was incorrect memory.
        print(f"Sample {i}: '{sample_text}' -> Vowel count: {result}")