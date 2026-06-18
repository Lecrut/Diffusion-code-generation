"""
Module to count vowels in a given string.

This module provides a utility function to accurately count the number of vowel characters ('a', 'e', 'i', 'o', 'u')
in any input string, regardless of case sensitivity or surrounding whitespace. It is designed for reuse within larger 
Python projects and adheres strictly to PEP 8 style guidelines.

Vowels considered: a, e, i, o, u (case-insensitive).

Author: Assistant AI
Date: October 2023
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowel characters in the provided string.

    This function iterates through each character in the input string and checks if it matches any of the standard 
    English vowels ('a', 'e', 'i', 'o', 'u'), treating both uppercase and lowercase letters as valid vowels. 

    Parameters
    ----------
    text : str
        The input string to analyze for vowel counts.

    Returns
    -------
    int
        The total count of vowel characters found in the string.

    Examples
    --------
    >>> count_vowels("Hello World")
    3
    >>> count_vowels("AEIOUaeiou")
    10
    
    Raises
    ------
    TypeError
        If 'text' is not a string instance.
    
    Notes
    -----
    - The function handles empty strings correctly, returning 0.
    - Non-alphabetic characters are ignored in the count but do not cause errors.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected 'str', got {type(text).__name__}")

    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Sample test cases running without external input or files.
    
    sample_1 = "Python is great!"
    count_1 = count_vowels(sample_1)

    sample_2 = ""
    count_2 = count_vowels(sample_2)

    sample_3 = "The quick brown fox jumps over the lazy dog."
    count_3 = count_vowels(sample_3)

    print(f"Vowel count in '{sample_1}': {count_1}")
    print(f"Vowel count in empty string: {count_2}")
    print(f"Vowel count in sample sentence: {count_3}")