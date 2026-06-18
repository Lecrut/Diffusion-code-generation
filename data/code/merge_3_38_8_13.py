"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which 
characters appear more than once, and returns them sorted alphabetically (case-sensitive).
It utilizes Python's built-in 'set' data structure for efficient duplicate detection.

Usage:
    The main execution block is provided with hard-coded sample values to demonstrate functionality.
"""

def find_repeated_characters(input_string):
    """
    Detects and lists all repeated characters in the given input string.
    
    Parameters:
        input_string (str): The string to analyze for duplicate characters.
        
    Returns:
        list[str]: A sorted list of unique characters that appear more than once 
                   in the input string. Characters are case-sensitive; 'A' and 'a' 
                   are treated as distinct unless both repeat independently or together.
    
    Example:
        >>> find_repeated_characters("hello world")
        ['d', 'e', 'h', 'l', 'o'] (Note: spaces might be included if repeated)
        
    Note:
        This implementation uses set operations to count occurrences efficiently.
        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(k), where k is the number of unique characters in the string.
    """
    
    # Create a set from the string for fast lookup and iteration over unique elements
    unique_chars = set(input_string)
    
    repeated_chars_set = []
    
    # Iterate through each character to check if it appears more than once
    for char in input_string:
        count = 0
        
        # Count occurrences of this specific character manually or via another method.
        # Since we need to know the frequency, a simple loop over unique_chars is efficient enough 
        # given typical string lengths, but counting directly within the set iteration logic below 
        # ensures accuracy without external dependencies like collections.Counter if strictly avoiding imports.
        
        # Alternative approach using list comprehension for clarity and standard library usage:
        # We will count occurrences by checking membership in a frequency map built implicitly or explicitly.
        # To adhere to "set operations" primarily, we can build the set first then check counts.
    
    # Re-implementing logic clearly with explicit counting based on unique elements found earlier
    
    char_counts = {}
    
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
        
    repeated_chars_list = []
    
    # Filter characters that have a count greater than 1 and sort them
    for char, count in sorted(char_counts.items()):
        if count > 1:
            repeated_chars_list.append(char)
            
    return repeated_chars_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    test_cases = [
        "hello world",      # Expected: ['d', 'e', 'h', 'l', 'o'] (space is not repeated)
        "aabbccdd",         # Expected: ['a', 'b', 'c', 'd']
        "abcdefg",          # Expected: [] (no repeats)
        "python programming", # Expected: [' ', 'p', 'r', 'o', 'n', 'm' is not repeated? wait. 
                            # p: 2, y:1, t:1, h:1, o:2, n:3, g:2, r:2, a:1, m:1
                            # Repeats: p, o, n, g, r] (space is repeated) -> [' ', 'g', 'n', 'o', 'p', 'r']
        "Mississippi",      # Expected: ['i', 's', 'p', 'M' no M repeat. i:4, s:4, p:2] -> ['i', 'p', 's']
    ]

    for test_input in test_cases:
        result = find_repeated_characters(test_input)
        print(f"Input: '{test_input}'")
        if not result:
            print("No repeated characters found.")
        else:
            # Joining the list to display as a string representation of unique chars for clarity
            output_str = "".join(result)
            print(f"Repeated characters (sorted): {output_str}")
        
        print("-" * 30)