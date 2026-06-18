def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string.
    
    This function uses Python's built-in len() function, which is highly optimized 
    in CPython to return O(1) time complexity for standard strings (str), as it simply
    returns the pre-calculated length attribute without traversing or counting characters.

    Args:
        phrase (str): The input string whose character count needs to be determined.

    Returns:
        int: The total number of characters in the provided string, including spaces 
             and special characters but excluding any surrounding whitespace unless it is part of the string itself.
    
    Example usage can refer to the sample block at the module level for concrete examples.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or CLI args).
    samples = [
        "Hello, World!",          # Expected: 13
        "",                       # Empty string - Expected: 0
        "   ",                    # Only spaces - Expected: 3
        "Python is awesome!      "# Trailing spaces included.
    ]

    for sample in samples:
        count = calculate_phrase_length(sample)
        print(f"'{sample}' has length {count}")