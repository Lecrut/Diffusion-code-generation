"""
Module to count vowels in a given string using Python 3 syntax.

This module provides utilities for counting vowel occurrences, adhering strictly 
to PEP 8 style guidelines for readability and maintainability in larger projects.

The main functionality is encapsulated within the ``count_vowels`` function, which 
accepts an input string (default: 'Hello World!') and returns the number of vowels 
found. The default argument ensures that a simple test case runs without requiring user 
input or command-line arguments.
"""

def count_vowels(text: str = "Hello World!") -> int:
    """
    Count the total number of vowels in the provided text string.

    This function iterates through each character in the input string and checks if it 
    matches any vowel (a, e, i, o, u), accounting for both uppercase and lowercase letters.

    Args:
        text (str): The input string to analyze. Defaults to 'Hello World!'.

    Returns:
        int: The count of vowels found in the text.

    Examples:
        >>> count_vowels("AEIOU")
        5
        
        >>> count_vowels("")
        0
    
    Note:
        This implementation uses a static list for vowel characters to ensure 
        efficiency and readability, avoiding redundant lookups or complex regex patterns.
    """

    # Define vowels as a set of single-character strings for O(1) lookup average complexity.
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    count: int = 0
    
    # Iterate over each character in the string to ensure type hints and explicit logic.
    for char in text.lower():
        if char in VOWELS:
            count += 1
            
    return count

if __name__ == '__main__':
    """
    Main execution block containing hard-coded sample values.

    This section demonstrates the usage of ``count_vowels`` with predefined inputs, 
    ensuring that the module runs without any user interaction or external dependencies.
    
    Sample tests verify basic functionality including:
        1. A standard sentence (Hello World!)
        2. An uppercase string (AEIOU)
        3. Mixed case input (Python Programming)
        4. Edge case with an empty string
    
    Output is printed directly to stdout for immediate verification in a script environment.
    """

    # Sample inputs provided as hard-coded constants per task requirements.
    SAMPLE_1 = "Hello World!"
    SAMPLE_2 = "AEIOU"
    SAMPLE_3 = "Python Programming"
    
    print("Vowel Count Results:")
    print(f"- \"{SAMPLE_1}\" has {count_vowels(SAMPLE_1)} vowel(s).")
    print(f"- \"{SAMPLE_2}\" has {count_vowels(SAMPLE_2)} vowel(s).")
    print(f'- "{SAMPLE_3}" has {count_vowels(SAMPLE_3)} vowel(s).')

    # Additional edge case test.
    empty_string = ""
    print(f'"{empty_string}" has {count_vowels(empty_string)} vowel(s).')
    
    # Final verification with default parameter (no explicit string passed).
    result_default = count_vowels()
    print(f"Default input '{SAMPLE_1}' matches expected logic: {result_default == 4}.")