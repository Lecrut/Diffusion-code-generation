def count_vowels(s: str) -> int:
    """
    Counts the occurrences of vowels in a string efficiently by iterating once.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        int: Total number of vowel characters found in the string.
    """
    if not isinstance(s, str):
        return 0

    # Set containing all vowels for O(1) lookup time
    vowels = set("aeiouAEIOU")
    
    count = 0
    
    # Single pass iteration through the string
    for char in s:
        if char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input or files are needed
    test_strings = [
        "Hello, World!",
        "aeiouAEIOU",
        "",
        "Python programming involves vowels like aeiou and AEIOU.",
        None  # Should handle non-string gracefully (though type check returns early)
    ]

    for test_str in test_strings:
        if isinstance(test_str, str):
            result = count_vowels(test_str)
            print(f"Input: '{test_str}' -> Vowel Count: {result}")