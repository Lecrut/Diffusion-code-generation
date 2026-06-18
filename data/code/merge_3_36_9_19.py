def reverse_string(s: str) -> str:
    """
    Reverses a string efficiently using Python's built-in slicing, 
    which correctly handles Unicode characters (including emojis, CJK characters, etc.).
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values covering various Unicode scenarios
    samples = [
        "Hello, World!",  # Basic ASCII with punctuation and space
        "\ud83d\ude02",     # Single emoji (Grinning Face) - ensures proper surrogate pair handling if needed by slice logic
        "你好世界",         # Chinese characters
        "🚀 \u4e16\u754c Hello",  # Mixed: Emoji, CJK, Latin mixed order
        "",                # Edge case: Empty string
        "\ud83d\ude0a"      # Another emoji variant (Smiling Face with Smiling Eyes)
    ]

    for original in samples:
        reversed_str = reverse_string(original)
        print(f'Original: {original!r}')
        print(f'Reversed : {reversed_str!r}\n')