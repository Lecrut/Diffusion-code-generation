"""
Count Vowels Module

This module provides a function to count the number of vowels in a given string,
case-insensitively. It is designed to be reusable within larger projects.

The implementation adheres strictly to PEP 8 style guidelines.

Vowel definition: 'a', 'e', 'i', 'o', 'u'. Case variations are included via the module constant.
"""

# Define vowels for clear usage and potential future extension (e.g., adding 'y')
_VOWELS = "aeiouAEIOU"

def count_vowels(text: str) -> int:
    """
    Count the total number of vowel characters in the input string.

    The function performs a case-insensitive check, treating both uppercase and lowercase
    vowels as equivalent for counting purposes. Non-vowel characters (including spaces, punctuation,
    digits, etc.) are ignored.

    Args:
        text (str): The input string to analyze. Can contain any type of character.

    Returns:
        int: The count of vowel occurrences in the text. If no vowels are found, returns 0.
             Handles empty strings gracefully by returning 0.

    Raises:
        TypeError: If the input is not a string instance (though Python's dynamic typing makes this
                  rare if used correctly as part of type hints).

    Examples:
        >>> count_vowels("Hello World")
        2
        >>> count_vowels("")
        0
        >>> count_vowels("AEIOU" * 10)
        50
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string type but got {type(text).__name__}")

    # Initialize counter and iterate directly over the string without converting to lowercase first.
    count = 0
    
    for char in text:
        # Check against predefined vowel set for efficiency and clarity
        if _VOWELS.count(char) > 0:
            count += 1
            
    return count

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without external input.
    
    samples = [
        "Hello, World!",
        "",
        "Python Programming",
        "AEIOUaeiou",
        "rhythm is silence"  # Note: 'y' and silent letters are not counted based on standard definition used here (a,e,i,o,u).
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' contains {result} vowel(s)")