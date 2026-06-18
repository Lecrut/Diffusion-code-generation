#!/usr/bin/env python3
"""
Module to calculate string length efficiently handling both ASCII and Unicode characters.

This module provides functionality to determine the number of characters in a given string,
ensuring compatibility with various character encodings including international scripts (e.g., 
Chinese, Japanese, Arabic) where single glyphs may occupy multiple bytes but count as one character.

Functions:
    calculate_string_length(s): Returns the length of the input string s using Python's built-in len().
"""

def calculate_string_length(s: str) -> int:
    """
    Calculate the number of characters in a given string.

    This function uses Python's native `len()` behavior, which counts Unicode code points (characters),
    not bytes or UTF-8 encoded units. It correctly handles ASCII and all supported Unicode scripts 
    without requiring external libraries like unicodedata for basic length calculation.

    Args:
        s (str): The input string whose length is to be calculated.

    Returns:
        int: The number of characters in the string.
    
    Example:
        >>> calculate_string_length("Hello")
        5
        >>> calculate_string_length("你好世界")
        4
        
    Note:
        Python strings are Unicode by default (since version 3.x). len() counts 
        individual grapheme clusters or code points depending on context, but typically 
        one character = one count for standard use cases like this.
        
    """
    return len(s)

if __name__ == '__main__':
    pass
