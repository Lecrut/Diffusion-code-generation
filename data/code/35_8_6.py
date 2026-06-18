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
        "aeiouAEIOU",         # Expected: 10
        "Rhythm is fun.",     # Expected: 3 (i, u - 'y' ignored as not in set)
        "No vowels here! @#$%",# Expected: 0
        "Python programming."#, Expected: 4 (o, o, i, a)
    ]

    for test_input in test_cases:
        result = count_vowels(test_input)
        print(f"Input: '{test_input}' -> Count: {result}")