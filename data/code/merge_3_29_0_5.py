#!/usr/bin/env python3
"""Script to reverse a given input string efficiently."""

def reverse_string(input_str: str) -> str:
    """Reverse the provided string using slicing, which is efficient in Python.
    
    Args:
        input_str (str): The string to be reversed. Handles empty strings 
                         and various character sets automatically.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_strings = [
        "",                                    # Empty string edge case
        "Hello, World!",                       # String with punctuation and spaces
        "Python3.9",                           # Numeric characters included
        "!@#$%^&*()_+-=[]{}|;:,.<>?/",       # Special characters only
    ]

    print("Reversed Strings:")
    for original in sample_strings:
        reversed_str = reverse_string(original)
        if len(reversed_str) == 0 or all(ord(c) <= 32 for c in reversed_str):
            print(f"Input: '{original}' | Output: '{reversed_str}'")
        else:
            print(f"Original: {original}")
            print(f"Reversed: {reversed_str}")