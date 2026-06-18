"""
Script to calculate the length of a given string efficiently handling both ASCII and Unicode characters.

This script defines two functions:
1. `calculate_string_length`: A robust function that calculates the number of code points in a string.
   It uses Python's built-in len() which is optimized for CPython but also works correctly with 
   standard strings (unicode) by counting individual characters/codepoints, ensuring efficiency and correctness 
   across different Unicode categories without needing external libraries like unicodedata for simple length calculation.

2. `calculate_codepoint_count`: An alternative implementation that explicitly iterates through the string
   to count code points using ord() logic, useful if one needs explicit control over counting characters vs bytes.
   
The script includes a main block with hard-coded sample values demonstrating usage without any user input or external dependencies.

Author: AI Assistant
Date: 2023-10-27
"""

def calculate_string_length(s):
    """
    Calculate the length of a string in terms of code points (characters).
    
    This function leverages Python's native behavior where strings are Unicode sequences 
    and len() counts the number of characters. For ASCII, this is 1 byte per char; for UTF-8 encoded 
    text represented as str objects, it still returns the character count correctly regardless of encoding size.

    Args:
        s (str): The input string to measure. Can contain any Unicode characters including emojis and special symbols.

    Returns:
        int: The number of code points in the string.
    
    Example:
        >>> calculate_string_length("Hello")
        5
        >>> calculate_string_length("🌍")
        1
        >>> calculate_string_length("Héllo Wörld")
        10 (assuming 'é' and 'ö' are single code points)
    """
    return len(s)

def calculate_codepoint_count_explicit(s):
    """
    Calculate the length of a string by explicitly iterating over characters.
    
    This is provided as an alternative implementation to demonstrate logic without relying solely on 
    built-in optimizations, though in practice `len()` is preferred for performance and readability.

    Args:
        s (str): The input string.

    Returns:
        int: Total count of code points.
    """
    return sum(1 for _ in s)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction or external inputs.
    
    test_cases = [
        "Hello, World!",  # ASCII string with spaces and punctuation
        "Café",           # String with accented character (Latin-1 supplement)
        "日本語",          # Japanese characters (CJK Unified Ideographs)
        "🌍🚀✨",         # Emojis (Surrogate pairs in Python strings, counted as 1 code point each by len())
        "",               # Empty string edge case
    ]

    print("String Length Calculation Results:")
    print("-" * 30)
    
    for test_string in test_cases:
        length = calculate_string_length(test_string)
        explicit_len = calculate_codepoint_count_explicit(test_string)
        
        # Verification that both methods yield the same result (they should always match for str objects)
        assert length == explicit_len, "Length calculation mismatch between built-in and explicit method."

        print(f"Input: {repr(test_string)}")
        print(f"Calculated Length: {length}")
        
        # Additional info on byte representation if needed (optional context)
        encoded_bytes = test_string.encode('utf-8')
        total_bytes = len(encoded_bytes)
        avg_bytes_per_char = round(total_bytes / length, 2) if length > 0 else 0
        
        print(f"UTF-8 Byte Length: {total_bytes}")
        print(f"Average Bytes per Character: {avg_bytes_per_char}")
        
        # Reset for next iteration (not strictly necessary in Python but good practice conceptually)
        pass

    print("-" * 30)
    print("All calculations completed successfully.")