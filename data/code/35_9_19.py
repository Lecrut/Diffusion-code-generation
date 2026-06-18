"""
Module to count vowels in a given string.

This module provides a function `count_vowels` that counts the number of vowel characters
in an input string, supporting both uppercase and lowercase letters (a, e, i, o, u).
It is designed for reuse in larger projects and adheres strictly to PEP 8 style guidelines.

No external dependencies are required. The function handles non-alphabetic characters by ignoring them.

Author: AI Assistant
Date: October 2023
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowel characters in a given string.

    This function iterates through each character in the input string and checks if it is a vowel.
    Vowels are defined as 'a', 'e', 'i', 'o', 'u' (case-insensitive). Non-vowel characters, including spaces,
    digits, punctuation, and letters outside this set, are ignored during counting.

    Args:
        text (str): The input string in which vowels need to be counted. Can contain any type of character.

    Returns:
        int: The total count of vowel characters found in the input string.

    Raises:
        TypeError: If the input is not a string instance.

    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("AEIOUaeiou123!")
        10
        >>> count_vowels("")
        0
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type, got {type(text).__name__}")

    vowels = set(['a', 'e', 'i', 'o', 'u'])
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "Python programming is fun.",
        "",
        "AEIOU",
        "bcdfg"
    ]

    for test_string in samples:
        result = count_vowels(test_string)
        print(f"'{test_string}' -> {result} vowels")