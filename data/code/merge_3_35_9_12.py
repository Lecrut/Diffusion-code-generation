"""
Module to count vowels in a given string.

This module provides a utility function `count_vowels` that counts the number of vowel characters
in an input string, supporting both uppercase and lowercase letters. It is designed to be reusable
within larger projects without requiring external dependencies or user interaction.

Vowel definition: 'a', 'e', 'i', 'o', 'u' (case-insensitive).

Author: Assistant
Date: 2023-10-27
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowel characters in the provided string.

    This function iterates through each character in the input string and checks if it is a vowel.
    The check is case-insensitive, meaning both 'A'/'a', 'E'/'e', etc., are counted as vowels.

    Args:
        text (str): The input string to analyze for vowel count.

    Returns:
        int: The total number of vowel characters found in the string.

    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("")
        0
    """
    vowels = set('aeiou')
    
    # Initialize counter and iterate over the string using enumerate for index tracking (optional utility)
    # However, simple iteration is sufficient. Using a generator expression with sum() ensures efficiency.
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    """
    Main execution block containing hard-coded sample values to demonstrate functionality.
    
    This section runs when the module is executed directly as a script, not imported.
    It does not require any user input or external resources.
    """

    # Sample test cases covering various scenarios: empty string, mixed case, no vowels, all vowels
    samples = [
        "Hello World",      # Expected: 2 (e, o)
        "AEIOU",            # Expected: 5
        "",                 # Expected: 0
        "Python Programming", # Expected: 4 (y is not counted here based on standard definition used in this module)
    ]

    print("Vowel Count Test Results:")
    for sample_text in samples:
        count = count_vowels(sample_text)
        status = f"Input: '{sample_text}' -> Output: {count}"
        # Note: In 'Python', standard vowels are y-o-n. If strict aeiou only, it's 1 ('o'). 
        # The implementation uses set('aeiou'), so 'y' is excluded.
        print(status)

    # Additional explicit test for the word "Vowels" itself to ensure clarity
    specific_test = "The vowels are A, E, I, O, U."
    result_count = count_vowels(specific_test)
    print(f"\nSpecific Test: '{specific_test}'")
    print(f"Total Vowel Count: {result_count}")