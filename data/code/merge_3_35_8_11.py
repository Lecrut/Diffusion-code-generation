def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel occurrences.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "Hello, World!",      # Expected: 2 (e, o)
        "aeiou",              # Expected: 5
        "1234567890",         # Expected: 0
        "Python Programming!",# Expected: 4 (y is not counted here based on strict aeiou definition, P,r,o,g,a,m are letters but only vowels count) -> Actually 'o', 'a' = 2. Let's re-evaluate sample logic carefully. 
                             # Sample: Python Programming!
                             # Vowels in "Python": o (1), y is usually not counted unless specified as vowel here, let's stick to aeiouAEIOU only.
                             # So 'o' -> 1.
                             # In "Programming": o, a = 2.
                             # Total: 3.
        "The quick brown fox jumps over the lazy dog", 
    ]

    for test_input in test_cases:
        result = count_vowels(test_input)
        print(f"Input: '{test_input}'")
        print(f"Vowel Count: {result}")
        print("-" * 20)