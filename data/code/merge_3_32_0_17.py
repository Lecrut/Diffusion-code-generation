#!/usr/bin/env python3
"""
Module to calculate the length of a string handling both ASCII and Unicode characters efficiently.

This module provides two functions:
1. `count_chars`: Counts the number of individual character units (code points) in a string.
   This is useful for counting visible glyphs like emojis or accented letters as single entities 
   if they are represented by one code point, but counts multi-byte UTF-8 sequences correctly.

2. `count_bytes`: Calculates the total byte length when the string is encoded to ASCII (if possible)
   or UTF-8. This reflects memory usage in Python 3 strings which store Unicode data internally 
   but serialize differently depending on encoding requirements.

The implementation uses standard library functions optimized for CPython and handles edge cases 
such as empty strings, mixed content, and surrogate pairs correctly by relying on the internal 
representation of string objects where available or falling back to explicit iteration if necessary
for maximum compatibility across Python versions (though primarily targeting 3.x).

Note: In modern Python 3 implementations, `len(string)` returns the number of Unicode code points.
However, this script explicitly demonstrates the logic for clarity and includes a byte counting utility 
to address potential ambiguities regarding 'length' in different contexts (character count vs bytes).
"""

def count_chars(s):
    """
    Returns the length of the string s as the number of Unicode code points.

    Args:
        s (str): The input string to measure. Can contain ASCII, extended ASCII, and full Unicode characters 
                 including emojis and combining marks.

    Returns:
        int: The count of individual character units in the string.

    Example:
        >>> count_chars("Hello")
        5
        >>> count_chars("🎉")
        1
        >>> count_chars("Café")
        4
    """
    # In Python, strings are Unicode sequences of code points (in CPython implementation).
    # The built-in len() function returns exactly the number of these code points.
    return len(s)

def count_bytes_utf8(s):
    """
    Returns the length of string s when encoded to UTF-8 bytes.

    This is useful for determining storage size in systems that rely on byte-level encoding 
    (e.g., database fields, network packets). It handles all valid Unicode characters correctly.

    Args:
        s (str): The input string to measure.

    Returns:
        int: The total number of bytes required to encode the string as UTF-8.

    Example:
        >>> count_bytes_utf8("Hello")
        5
        >>> count_bytes_utf8("🎉")
        4 (Emoji typically takes 3 or 4 bytes in UTF-8)
        >>> count_bytes_utf8("Café")
        6 ('é' is 2 bytes: 0xC3 0xA9)
    """
    # Encode the string to UTF-8 and return the length of the resulting byte sequence.
    # This operation is efficient in CPython as it delegates to optimized internal codecs.
    try:
        encoded = s.encode('utf-8')
        return len(encoded)
    except UnicodeEncodeError:
        raise ValueError("Input string contains invalid or unencodable characters for UTF-8.")

def count_bytes_ascii(s):
    """
    Returns the length of string s when strictly attempted to be represented as ASCII bytes.

    Note: This will only succeed if all characters in the string are within the 0x00-0x7F range.
    If non-ASCII characters are present, it raises a ValueError.

    Args:
        s (str): The input string to measure. Must contain only ASCII characters.

    Returns:
        int: The count of bytes if all characters are valid ASCII.

    Raises:
        ValueError: If the string contains any non-ASCII character.

    Example:
        >>> count_bytes_ascii("Hello")
        5
        >>> count_bytes_ascii("Café")
        Traceback (most recent call last):
            ...
        ValueError: String contains non-ASCII characters.
    """
    # Check if all characters are in the ASCII range before encoding to ensure no errors occur silently or raise early.
    for char in s:
        if ord(char) > 127:
            raise ValueError("String contains non-ASCII characters.")
    
    return len(s.encode('ascii'))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello World",           # Standard ASCII string
        "Café résumé",          # String with accented characters (Latin Extended)
        "🎉 Happy New Year 🚀", # String containing emojis and mixed content
        "",                     # Empty string edge case
        "1234567890!"           # Digits and symbols
    ]

    print("String Length Calculation Module")
    print("=" * 40)

    for text in samples:
        char_len = count_chars(text)
        
        try:
            ascii_bytes = count_bytes_ascii(text)
            byte_info = f"ASCII bytes: {ascii_bytes}"
        except ValueError as e:
            # If ASCII conversion fails, we still report the UTF-8 length but note it's not pure ASCII.
            utf8_bytes = count_bytes_utf8(text)
            ascii_bytes = None
            byte_info = f"Not Pure ASCII (UTF-8 bytes: {utf8_bytes})"

        print(f"\nInput: \"{text}\"")
        print(f"Character Count (Unicode code points): {char_len}")
        
        if ascii_bytes is not None:
            print(f"ASCII Byte Length: {ascii_bytes} ({byte_info})")
        else:
            utf8_bytes = count_bytes_utf8(text)
            print(f"UTF-8 Byte Length: {utf8_bytes} ({byte_info.replace('Not Pure ASCII', '')})")

    # Demonstrate error handling for non-ASCII in pure ASCII mode
    try:
        _ = count_bytes_ascii("Test🎉")
    except ValueError as e:
        print(f"\nError demonstration (non-ASCII in ASCII check): {e}")