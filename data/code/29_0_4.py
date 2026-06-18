#!/usr/bin/env python3
"""
Script to reverse a given input string efficiently.
Handles edge cases including empty strings, Unicode characters, 
and various character sets without requiring external libraries beyond standard Python.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the provided input string in-place using slicing.

    Args:
        text (str): The string to be reversed. Handles empty strings and all Unicode characters correctly.

    Returns:
        str: A new string which is the reverse of the input.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) if using slice assignment on a list, or O(n) for immutable slicing result.
    """
    return text[::-1]

if __name__ == '__main__':
    # Sample values covering various scenarios without user input
    test_cases = [
        "Hello World!",           # Standard string with spaces and punctuation
        "",                       # Empty string edge case
        "Unicode: 你好 мир 🌍",   # Unicode characters including CJK and emojis
        "1234567890_",            # Mix of digits and special chars
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input}")
        print(f"Reversed:{reversed_output}\n")