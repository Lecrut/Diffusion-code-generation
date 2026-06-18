"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which 
characters appear more than once, and returns them along with their counts.
It utilizes Python's built-in 'set' data structure for efficient duplicate detection.

Usage:
    The main execution block includes hard-coded sample strings to demonstrate functionality.
"""

def find_repeated_characters(input_string):
    """
    Detects all repeated characters in the given input string and returns a dictionary 
    mapping each character to its count. Only characters with counts greater than 1 are included.

    Args:
        input_string (str): The string to analyze for duplicate characters.

    Returns:
        dict: A dictionary where keys are characters found more than once, 
              and values represent the number of occurrences of that character in the original string.
    
    Example:
        >>> find_repeated_characters("hello world")
        {'l': 3, 'o': 2}
    """
    # Convert input to lowercase for case-insensitive comparison if desired, 
    # though the problem implies exact match unless specified otherwise. 
    # We will perform a case-sensitive check as per standard string processing norms 
    # unless told to ignore case. However, often "characters" implies ignoring case in natural language tasks.
    # To be robust and follow typical expectations for such problems: we treat 'A' and 'a' as distinct 
    # unless specified otherwise (e.g., "case-insensitive"). The prompt does not specify case handling.
    # Let's stick to exact character matching based on the string provided.

    char_count = {}
    
    # Iterate over each character in the input string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Filter out characters that are not repeated (count must be > 1) and convert to sorted list of tuples or dict items
    repeated_chars_dict = {char: count for char, count in char_count.items() if count > 1}

    return repeated_chars_dict

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    # Sample Input String: "programming"
    sample_input_1 = "programming"
    
    # Another Sample Input String with spaces and punctuation for variety (if needed)
    # Let's use a string similar to the example in comments but distinct from above 
    # or just extend it. Here we'll keep it simple as per task description.
    sample_input_2 = "hello world"

    print("Sample 1 Analysis:", find_repeated_characters(sample_input_1))
    print("Sample 2 Analysis:", find_repeated_characters(sample_input_2))