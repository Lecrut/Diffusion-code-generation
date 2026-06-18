#!/usr/bin/env python3
"""
Script to capitalize the first letter of each word in a string while preserving other casing.
Uses efficient built-in methods without external libraries or interactive input.
"""

def title_case_string(text: str) -> str:
    """
    Capitalizes only the first character of every alphabetic sequence (word).

    Args:
        text: Input string to process.

    Returns:
        New string with each word's first letter capitalized and rest unchanged.
    
    Example:
        "hello world  Hello WORLD" -> "Hello World  Hello World"
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    result_parts = []
    current_word_start = False

if __name__ == '__main__':
    pass
