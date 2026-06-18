def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, case-insensitive.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters ('a', 'e', 'i', 'o', 'u').
    """
    if not isinstance(text, str):
        return 0
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Using a set for O(1) lookup time makes this efficient even for long strings.
    count = sum(1 for char in text.lower() if char in vowels)
    
    return count

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure the module runs without input or files.
    sample_strings = [
        "Hello, World!",      # Expected: 2 (e, o)
        "AEIOUaeiou",         # Expected: 10
        "Python3 Programming.", # Expected: 4 (y is not a vowel in this context per standard definition used here; actually 'o' and 'i'. Let's re-evaluate: P-y-t-h-o-n-3-P-r-o-g-r-a-m-m-i-ng. Vowels: o, o, a, i = 4)
        "12345",              # Expected: 0 (non-alphabetic handled gracefully)
        "",                   # Expected: 0 (empty string)
    ]

    for test_input in sample_strings:
        result = count_vowels(test_input)
        print(f"'{test_input}' -> {result}")