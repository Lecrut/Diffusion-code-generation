"""
Script to calculate the length of a given string handling both ASCII and Unicode characters efficiently.
This script uses Python's built-in len() function which correctly handles Unicode strings by counting 
the number of code points (characters) rather than bytes or runes in older implementations, ensuring
accurate representation for international text.

Note: This module does not require any user input, command-line arguments, network access, or pre-existing files.
"""

def calculate_string_length(text):
    """
    Calculates the length of a string by counting its code points.
    
    Args:
        text (str): The input string to measure. Can be ASCII or Unicode.
        
    Returns:
        int: The number of characters in the string.
    """
    # Python's len() function on strings returns the length in terms of unicode_code_points,
    # which is efficient and handles all valid UTF-8/Unicode text correctly.
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    
    samples = [
        "Hello",                          # Standard ASCII string
        "你好世界",                       # Chinese characters (2 code points per char in some encodings, but len counts 4)
        "Héllo Wörld 🎉",                # Mixed Latin with diacritics and emoji (emoji is multiple code points)
        "",                              # Empty string edge case
    ]

    for sample_text in samples:
        length = calculate_string_length(sample_text)
        print(f"String: '{sample_text}'")
        print(f"Length: {length}")
        
    # Additional explicit test with a complex Unicode character (e.g., combining diacritical marks)
    complex_char_test = "naïve\n\u0627\u064a\u0631\u06cc\u0691y \u200b"  # Arabic text + zero-width space
    length_complex = calculate_string_length(complex_char_test)
    
    print("\nComplex Unicode Test:")
    print(f"String: '{complex_char_test}'")
    print(f"Length (code points): {length_complex}")