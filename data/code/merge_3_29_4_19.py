def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates over the input string and constructs a new string 
    with characters added from last to first. It properly handles all Unicode 
    code points including emojis, combining characters, and non-Latin scripts.

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Unicode character.

    Returns:
        str: A new string containing the characters of the original string in reverse order.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🌍 world")
        'dlrow 🌍'
    """
    return ''.join(reversed(s))

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required.
    sample_strings = [
        "hello",
        "Unicode: 你好世界",
        "🚀 🌍 ☕️",
        "",
        "A" * 100 + "B"
    ]

    for test_input in sample_strings:
        result = reverse_string(test_input)
        print(f"Input:    {repr(test_input)}")
        print(f"Output:   {repr(result)}")
        print("-" * 40)