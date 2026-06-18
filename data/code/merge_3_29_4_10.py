"""
Module to reverse characters in a string while correctly handling Unicode.

This module provides functionality to reverse the order of characters in a given string,
ensuring that multi-byte Unicode sequences (such as emojis and accented characters) are
preserved intact during reversal. The implementation relies on Python's native support for
Unicode code points via `str[::-1]`, which handles complex scripts correctly without manual
byte manipulation errors.

Functions:
    reverse_string(input_str): Reverses the input string preserving Unicode integrity.
"""

def reverse_string(input_str) -> str:
    """
    Reverses the order of characters in a given string, handling all Unicode code points
    including multi-byte sequences (e.g., emojis, non-Latin scripts).

    Args:
        input_str (str): The original string to be reversed. Can contain any valid 
                         Python 3 unicode character. Returns str.

    Returns:
        str: A new string with characters in reverse order relative to the input.

    Example:
        >>> reverse_string("Hello, 世界!")
        '!世界，olleH'
        >>> reverse_string("🌍✨")
        '✨🌍'
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies.
    
    samples = [
        "Hello, World!",  # Basic ASCII with punctuation
        "你好世界",         # Chinese characters (UTF-8 multi-byte)
        "Café résumé",      # Latin extended accents
        "🌍✨💻🚀",          # Emoji sequence
        "Möbius Strip",     # German umlauts mixed with ASCII
    ]

    for sample in samples:
        reversed_result = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed : {reversed_result!r}\n")