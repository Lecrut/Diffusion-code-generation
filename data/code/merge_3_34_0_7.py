#!/usr/bin/env python3
"""
Script to capitalize only the first letter of each word in a string,
preserving the rest of the casing. It uses efficient string manipulation
without external dependencies or interactive prompts.
"""

def capitalize_words(s: str) -> str:
    """
    Capitalizes the first character of each word while preserving case for 
    subsequent characters within that word.

    Parameters:
        s (str): The input string.

    Returns:
        str: A new string with only the first letter of each word capitalized.
    
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python3 is fun")
        'Python3 Is Fun'
        >>> capitalize_words("")
        ''
        >>> capitalize_words("no spaces here")
        'No Spaces Here'
    """
    
    if not s:  # Handle empty string efficiently without creating intermediate lists for edge cases.
        return ""

    result_chars = []
    
    word_started = False

if __name__ == '__main__':
    pass
