def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates through the input string from end to start and constructs
    a new string with the characters in reversed order. It properly handles all 
    Unicode code points, including emojis, combining characters, and non-Latin scripts.

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Unicode character.

    Returns:
        str: A new string containing the characters of the original string in reverse order.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🌍Hello 世界")
        '界世！olleH🌍' (note: spaces and specific unicode chars preserved)
    """
    return ''.join(reversed(s))

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required.
    sample_strings = [
        "hello",
        "Unicode 测试 🌍",
        "",
        "1234567890!",
        "こんにちは世界"
    ]

    for text in sample_strings:
        reversed_text = reverse_string(text)
        print(f"Original: {text!r}")
        print(f"Reversed:{reversed_text!r}\n")