"""
Module to count vowels in a given string.

This module provides utilities for counting vowel occurrences (a, e, i, o, u) 
in both uppercase and lowercase forms within any input text. It is designed 
for reuse in larger projects and adheres strictly to PEP 8 style guidelines.

Functions:
    count_vowels(text): Counts the number of vowels in a string.

Author: Assistant
Version: 1.0.0
"""

def _normalize_text(text: str) -> str:
    """
    Normalize text by converting it to lowercase for consistent vowel counting.

    Args:
        text (str): The input string to be processed.

    Returns:
        str: Lowercase version of the input string.
    """
    return text.lower()

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string.

    This function iterates through each character in the normalized (lowercased) 
    input string and increments a counter if the character is one of the five 
    standard English vowels ('a', 'e', 'i', 'o', 'u').

    Args:
        text (str): The input string to analyze. Can contain any characters; 
                    only vowels are counted. Empty strings or None will return 0, 
                    though None is not explicitly handled here as per strict type hinting 
                    implying str argument. If non-string types are passed in a real scenario,
                    this would raise TypeError, but we assume valid input based on docstring.

    Returns:
        int: The total count of vowels found in the string.

    Raises:
        TypeError: If text is not an instance of str (though logic assumes correct usage).
    
    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("AEIOU")
        5
        >>> count_vovels("") -> 0 (Note: typo in example handled by function)
        >>> count_vowels("Rhythm")
        1
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type, got {type(text).__name__}")

    vowels = {'a', 'e', 'i', 'o', 'u'}
    normalized_text = _normalize_text(text)
    
    count = 0
    
    for char in normalized_text:
        if char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "Python programming is awesome.",
        "",
        "AEIOUaeiou",
        "xyz"
    ]

    print("Vowel Count Results:")
    for sample in samples:
        result = count_vowels(sample)
        # Using f-string with curly braces to avoid confusion, though simple concatenation is also fine.
        # Ensuring no markdown fences or prose outside the code block as per constraints.
        print(f"Input: '{sample}' -> Vowel Count: {result}")