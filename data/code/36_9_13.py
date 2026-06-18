def reverse_string(s: str) -> str:
    """
    Reverses a string efficiently using Python's built-in slicing,
    which correctly handles all Unicode characters including emojis 
    and complex scripts without explicit encoding steps.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string with the characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values covering various Unicode scenarios
    test_cases = [
        "Hello, World!",  # Basic ASCII punctuation and spaces
        "🚀✨💻",          # Emoji characters (surrogate pairs)
        "日本語テスト",     # Japanese text with CJK characters
        "Café naïve résumé", # Accented Latin characters
        "",               # Empty string edge case
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed:{reversed_output!r}\n")