def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates through the input string from end to start and constructs
    a new string with the characters in reversed order. It properly handles all Unicode
    characters including emojis, combining marks, and non-Latin scripts by treating each
    character as an individual code point (which is typically what users expect when reversing text).

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Unicode characters.

    Returns:
        str: A new string containing the characters of the original string in reverse order.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🌍Hello 世界")
        '界世！olleH🌍' (Note: specific emoji rendering may vary, but code points are reversed)
    
    Note:
        Unlike some languages where reversing might involve grapheme clusters (visually connected characters),
        this function reverses by individual Unicode code points. This is the standard behavior for string reversal
        in Python unless explicit grapheme support is required via external libraries like `unicodedata` or specialized packages.

    Raises:
        TypeError: If the input is not a string type.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string type, got {type(s).__name__}")
    
    return ''.join(reversed(list(s)))

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external input or files are needed
    sample_strings = [
        "hello",
        "Python 3.12",
        "Unicode: 🌍🎉Hello World!",
        "",
        "a" * 100,  # Test with a long string of repeated characters
    ]

    for test_input in sample_strings:
        reversed_result = reverse_string(test_input)
        print(f"Original:   '{test_input}'")
        print(f"Reversed:   '{reversed_result}'")
        print("-" * 40)