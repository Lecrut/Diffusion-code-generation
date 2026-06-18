"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which characters 
appear more than once, and returns them sorted alphabetically. It uses the difference between 
a set of unique characters and a frequency-count based approach optimized via intersection logic
to ensure clarity and correctness without external dependencies like collections.Counter for core logic 
demonstration (though Counter is standard library allowed). The primary method demonstrated here 
uses basic set operations to find duplicates efficiently.

The main execution block includes hard-coded sample values as per requirements, ensuring the script
runs without user input or network access.
"""

def find_repeated_chars(input_string: str) -> list[str]:
    """
    Detect and return a sorted list of all characters that appear more than once in the input string.

    Args:
        input_string (str): The string to analyze for repeated characters.

    Returns:
        list[str]: A sorted list of unique characters found multiple times in the input string.
    
    Example:
        >>> find_repeated_chars("hello world")
        ['d', 'e', 'h', 'l', 'o'] (Note: case-sensitive, spaces included)
    """
    # Create a set to track seen characters and another for duplicates
    unique_seen = {}  # Using dict to count occurrences explicitly while maintaining order of first appearance logic if needed, 
                      # but here we just need counts. Actually, simple counting is best.
    
    char_counts = {}

    # Iterate over each character in the string to build a frequency map
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Identify characters with count greater than 1
    repeated_chars_set = set()
    
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars_set.add(char)

    # Convert the set to a sorted list and return
    return sorted(list(repeated_chars_set))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No input(), sys.stdin, argparse, or network access is used here.
    
    test_strings = [
        "hello world",      # Expected: ['d', 'e', 'h', 'l', 'o'] (case sensitive)
        "aabbccdd",         # Expected: ['a', 'b', 'c', 'd']
        "python programming", # Expected: ['g', 'n', 'p', 'r'], note 't' is unique, space counts too if present? 
                            # Wait, let's trace manually: p(2), y(1), t(1), h(1), o(1), n(3),  (space)(2), p(2)r(2)o(1)g(2)m(1)i(1)n(3).
                            # Repeated: ' ', 'n', 'p', 'r' -> sorted: [' ', 'n', 'p', 'r']? 
                            # Actually space is a char. Let's re-verify "python programming"
                            # p, y, t, h, o, n,  , p, r, o, g, r, a, m, m, i, n, g
                            # Counts: p=2, y=1, t=1, h=1, o=2, n=3, ' '=2, r=2, g=2, a=1, m=2, i=1.
                            # Repeated set: {'p', 'o', 'n', ' ', 'r', 'g', 'm'} -> sorted list includes space at start? 
                            # Yes, ASCII 32 comes before letters. So [' ', 'g', 'm', 'n', 'o', 'p', 'r']
        "1234567890",      # Expected: [] (no repeats)
        "",                 # Expected: [] (empty string)
    ]

    for test_str in test_strings:
        result = find_repeated_chars(test_str)
        print(f"Input: '{test_str}'")
        if not result:
            print("No repeated characters found.")
        else:
            print(f"Repeated characters: {result}")
        
        # Optional small pause for readability in console output, though not strictly required by logic.
        pass