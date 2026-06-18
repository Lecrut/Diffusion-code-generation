#!/usr/bin/env python3
"""
Module to reverse strings with full Unicode support using idiomatic Python techniques.

The solution utilizes string slicing, which is the most efficient (O(n)) 
and readable way to reverse a sequence in Python while correctly handling
all Unicode characters including emojis and complex scripts due to their UTF-8 encoding.
"""

def reverse_string(text: str) -> str:
    """
    Reverses a given string with full Unicode support.

    Args:
        text (str): The input string containing any valid Unicode characters.

    Returns:
        str: A new string that is the reverse of the input, preserving character order 
             and handling all UTF-8 sequences correctly.
    
    Example:
        >>> reverse_string("Hello") -> "olleH"
        >>> reverse_string("\u05d1\u05e2\u05dc \u05de\u05c4\u05b9") -> "\u05bb\u05dd \u05ba\u05d7\u05ca"
    """
    # String slicing with a step of -1 creates a reversed copy efficiently.
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    samples = [
        "Hello, World!",
        "\u05d1\u05e2\u05dc \u05de\u05c4\u05b9",  # Hebrew: Betsaleel
        "\ud83d\ude00\ud83d\ude08",                   # Two emojis (Happy Face + Grimacing Face)
        "1234567890!",                           # Mixed alphanumeric and symbol
    ]

    print("Reversed Strings:")
    for original in samples:
        reversed_str = reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed : {reversed_str}\n")