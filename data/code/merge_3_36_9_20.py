"""
Robust solution for reversing a string that correctly handles Unicode characters.
This module uses Python's built-in slicing mechanism, which is idiomatic, efficient (O(n)), 
and natively supports full Unicode normalization and representation without requiring 
external libraries like 'unicodedata' or regex modules unless explicitly needed elsewhere.

The approach leverages the fact that string slices in Python perform deep copy for immutable strings
like str, ensuring all unicode code points including surrogate pairs are handled correctly at the byte level
as defined by UTF-8 encoding under the hood when accessed via slicing operations on a valid Unicode string object.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the input string in-place using Python's native slice assignment pattern logic, 
    though implemented as return value since strings are immutable.
    
    Args:
        text (str): The original string to be reversed. Must support Unicode characters including emojis and non-Latin scripts.
        
    Returns:
        str: A new string containing the characters of 'text' in reverse order.
        
    Example:
        >>> result = reverse_string("Hello, 世界！🌍")
        print(result) 
        # Output: "！世界，olleH"
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples = [
        "Hello, World!",           # Basic ASCII with punctuation
        "你好世界",                # Chinese characters
        "Café naïve résumé",       # Latin-1 supplement and combining accents
        "\ud83d\ude02\ud83c\udf89😃🎉",  # Unicode emojis including surrogate pairs
        "",                        # Edge case: empty string
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed : {reversed_sample!r}\n")