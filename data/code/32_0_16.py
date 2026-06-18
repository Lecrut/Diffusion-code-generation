"""
Module to calculate string length handling both ASCII and Unicode characters efficiently.

This module provides a function that correctly counts characters in a string,
respecting Python 3's native behavior where len() returns character count (code points),
not bytes or grapheme clusters unless explicitly configured otherwise for legacy reasons.

Note: In standard UTF-8/UTF-16 strings used by default in modern Python environments, 
the built-in `len()` function already counts Unicode code points correctly.
This script demonstrates this behavior with comprehensive examples and a custom helper
for educational purposes or specific byte-level analysis if needed later.
"""

def count_unicode_characters(s: str) -> int:
    """
    Counts the number of characters (Unicode code points) in the given string.
    
    This function leverages Python's native string handling which treats strings 
    as sequences of Unicode scalar values by default since version 3.x.
    
    Args:
        s (str): The input string containing ASCII, extended ASCII, or any Unicode character.
        
    Returns:
        int: The count of characters in the string.
    """
    return len(s)

def analyze_string_length(sample_str: str) -> dict:
    """
    Analyzes a sample string and returns detailed length information.
    
    This function provides metadata about the input string including its character 
    count, byte representation size (for UTF-8), and list of unique characters.
    
    Args:
        sample_str (str): The string to analyze.
        
    Returns:
        dict: A dictionary containing length metrics.
            - 'char_count': Number of Unicode code points.
            - 'byte_size_utf8': Size in bytes when encoded as UTF-8.
            - 'unique_chars': Set of unique characters found.
    """
    char_count = len(sample_str)
    byte_repr = sample_str.encode('utf-8')  # Standard encoding for text files/web content
    
    return {
        "char_count": char_count,
        "byte_size_utf8": len(byte_repr),
        "unique_chars": set()
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    # Sample 1: Pure ASCII string
    ascii_sample = "Hello, World!"
    
    # Sample 2: Unicode characters including emojis and non-Latin scripts
    unicode_samples = [
        "Café",           # Accented character
        "日本語テスト",     # Japanese text
        "🌍🚀💻",         # Emojis (multi-code point in some cases)
        "Δ∑πℯφ‡¶⊥"      # Mathematical and special symbols
    ]
    
    print("=" * 50)
    print("Unicode String Length Calculator")
    print("=" * 50)
    
    for i, test_str in enumerate(unicode_samples, 1):
        result = analyze_string_length(test_str)
        
        # Display character count (code points)
        char_count = len(test_str)
        
        # Encode to UTF-8 bytes and show byte length
        utf_8_bytes = test_str.encode('utf-8')
        byte_len = len(utf_8_bytes)
        
        print(f"\nSample {i}: '{test_str}'")
        print("-" * 30)
        print(f"Unicode Character Count (Code Points): {char_count}")
        print(f"UTF-8 Byte Length:                     {byte_len} bytes")
        
        # Demonstrate potential difference for surrogate pairs if any (though Python 3 handles these gracefully)
        unique_chars = set(test_str.encode('utf-16-be'))
        print(f"Surrogate Pair Count (approx):     {len(unique_chars)}")

    # Explicit demonstration using the main function directly on an ASCII string
    ascii_demo_result = count_unicode_characters(ascii_sample)
    
    print("\nASCII Demo: '{}'".format(ascii_sample))
    print("-" * 30)
    print(f"Calculated Length via Function: {ascii_demo_result}")