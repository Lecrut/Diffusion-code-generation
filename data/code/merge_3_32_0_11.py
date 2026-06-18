#!/usr/bin/env python3
"""
Module to calculate string length handling both ASCII and Unicode characters efficiently.

This module defines a function that returns the number of Unicode code points in a given string,
which is equivalent to Python's built-in `len()` function for strings but explicitly documented
for clarity regarding UTF-8/Unicode representation versus byte count.

It also includes an efficient method to calculate length based on character encoding if needed,
though standard len() is the most optimized approach in modern CPython implementations.

The script avoids external dependencies and interactive input as per requirements.
"""

def calculate_unicode_length(s: str) -> int:
    """
    Calculate the number of Unicode code points (characters) in a string.

    This function effectively delegates to Python's built-in len() which is implemented 
    in C and handles UTF-8 strings efficiently by counting characters, not bytes.
    
    Args:
        s (str): The input string whose length needs to be calculated.
        
    Returns:
        int: The number of Unicode code points in the string.

    Example:
        >>> calculate_unicode_length("Hello")
        5
        >>> calculate_unicode_length("🚀✨")
        2 (two emoji characters)
    """
    return len(s)

def get_byte_length(s: str, encoding: str = 'utf-8') -> int:
    """
    Calculate the length of a string in bytes given a specific encoding.

    This is useful for network transmission or file storage where byte count matters.

    Args:
        s (str): The input string.
        encoding (str): The character encoding to use ('utf-8', 'ascii', etc.). Default is 'utf-8'.
        
    Returns:
        int: The number of bytes required to represent the string in the specified encoding.

    Raises:
        LookupError: If an invalid encoding name is provided.
    
    Example:
        >>> get_byte_length("Hello", "ascii")
        5
        >>> get_byte_length("🚀✨", "utf-8")
        12 (approximate depending on specific emoji code points)
    """
    import codecs
    
    try:
        return len(s.encode(encoding))
    except LookupError as e:
        raise ValueError(f"Invalid encoding provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    samples = [
        "Hello, World!",         # ASCII text
        "Café",                  # Contains accented character (Unicode)
        "🚀✨🌍",                # Emoji characters (Multilingual Plane + Supplementary Planes)
        "",                     # Empty string
        "1234567890"            # Digits only
    ]

    print("String Length Calculation Results")
    print("-" * 30)

    for sample in samples:
        char_len = calculate_unicode_length(sample)
        byte_len_utf8 = get_byte_length(sample, 'utf-8')
        
        status_msg = "ASCII only" if all(ord(c) < 128 for c in sample) else f"{len([c for c in sample if ord(c) >= 128])} Unicode char(s)"

        print(f'String: "{sample}" (Length {status_msg})')
        print(f'Unicode Code Point Count: {char_len}')
        print(f'UTF-8 Byte Count: {byte_len_utf8}')
        
        if sample == "":
            print("-" * 30)