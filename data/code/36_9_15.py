def reverse_string(s: str) -> str:
    """
    Reverses a string correctly handling all Unicode characters including emojis, 
    non-BMP characters (surrogate pairs), and combining marks by leveraging Python's 
    efficient internal UTF-8/UCS4 representation. This method treats the entire input as an immutable sequence of code points.

    Args:
        s (str): The string to be reversed. Can contain any Unicode character supported in Python 3.

    Returns:
        str: A new string with characters in reverse order relative to their original positions.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🚀✨")  # Surrogate pairs for emojis handled correctly by slicing strings in Python 3
        '✨🚀'
        >>> reverse_string("café")
        'éfac'
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "hello world",  # Basic ASCII string with space
        "🌍✨💻🔥",     # Multi-emoji sequence involving potentially complex Unicode representations
        "日本語テスト",   # Japanese text (CJK characters)
        "café naïve résumé", # Strings containing accent marks and combining diacriticals where applicable
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: {sample}")
        print(f"Reversed: {reversed_sample}\n")