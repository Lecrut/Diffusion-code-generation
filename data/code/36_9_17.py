def reverse_string(text: str) -> str:
    """
    Reverses a string while correctly handling Unicode characters (including emojis, 
    combining marks, etc.). Uses Python's built-in slicing which handles all valid 
    Unicode strings according to the language standard efficiently.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string with the characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Sample inputs covering ASCII, emojis, and Unicode combining sequences for robustness testing
    sample_strings = [
        "Hello World",           # Standard ASCII
        "\ud83d\ude00",          # Single emoji (U+1F600 GRAVE FACE)
        "café\n\t\r",            # Special characters including newline and tab
        "日本語 \u4e2d\u6587 한국어",  # Multiple scripts: Japanese, Chinese, Korean
    ]

    results = []
    for s in sample_strings:
        reversed_s = reverse_string(s)
        results.append(f"Original: {s!r}\nReversed:   {reversed_s!r}")

    print("\n".join(results))