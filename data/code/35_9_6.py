"""
Module to count vowels in a given text string.

This module provides utilities for counting vowel occurrences (a, e, i, o, u)
in both uppercase and lowercase forms within arbitrary strings. It is designed
for reuse in larger projects and adheres strictly to PEP 8 style guidelines.

Functions:
    count_vowels(text): Counts the number of vowels in a string.
"""

def count_vowels(text: str) -> int:
    """
    Count the total number of vowels (a, e, i, o, u) in the provided text.

    This function is case-insensitive and counts both uppercase and lowercase
    vowel occurrences. It ignores all other characters including spaces, digits,
    punctuation, and special symbols.

    Args:
        text (str): The input string to analyze for vowels.

    Returns:
        int: The total count of vowels found in the input string.

    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("AEIOUaeiou123!")
        10
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type, got {type(text).__name__}")

    vowels = set('aeiou')
    
    # Using a generator expression with sum for memory efficiency on large strings
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "The quick brown fox jumps over the lazy dog.",
        "AEIOUaeiou123!@#",
        "",
        "No vowels here",
        "Vowels: aeiou"
    ]

    for sample in samples:
        count = count_vowels(sample)
        print(f"'{sample}' contains {count} vowel(s).")