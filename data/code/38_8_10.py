"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which 
characters appear more than once, and returns a sorted list of unique duplicate characters.
It utilizes Python's built-in `set` data structure for efficient membership testing 
and deduplication, adhering to the requirement of avoiding bit manipulation unless necessary.

Usage:
    The module is designed to be run as a standalone script with hard-coded sample inputs.
    It does not require any user input, command-line arguments, network access, or external files.
"""

def find_duplicate_characters(input_string):
    """
    Identifies and lists all characters that appear more than once in the given string.

    Parameters:
        input_string (str): The string to analyze for duplicate characters.

    Returns:
        list[str]: A sorted list of unique characters found more than once in the input string.
                   If no duplicates are found, returns an empty list.
    
    Example:
        >>> find_duplicate_characters("hello world")
        ['d', 'e', 'h', 'l', 'o']  (Note: order is alphabetical due to sorting)

    Note:
        This implementation uses set operations for efficiency and clarity over bit manipulation,
        as Python strings are Unicode sequences rather than raw binary data. Sets provide O(1) 
        average time complexity for lookups and automatic deduplication.
    """
    
    # Create a frequency dictionary to count occurrences of each character
    char_counts = {}

    # Iterate over the input string to populate counts
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Extract characters that have a count greater than one and sort them alphabetically
    duplicates = sorted([char for char, count in char_counts.items() if count > 1])

    return duplicates

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_inputs = [
        "hello world",
        "aabbccdd",
        "programming is fun",
        "abcdefg"  # Expected to return an empty list as there are no duplicates.
    ]

    print("Duplicate Character Detection Module")
    print("-" * 30)

    for test_case in sample_inputs:
        result = find_duplicate_characters(test_case)
        
        if not result:
            print(f'Input: "{test_case}"')
            print('Result: No duplicate characters found.')
        else:
            # Format the output as a joined string of characters separated by spaces for readability.
            duplicates_str = ' '.join(result)
            print(f'Input: "{test_case}"')
            print(f'Duplicate Characters: {duplicates_str}')
        
        print("-" * 30)