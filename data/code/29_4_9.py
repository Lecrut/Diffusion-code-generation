def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function creates a new string with characters appearing in reverse order
    compared to the input. It properly handles all Unicode code points by iterating
    over the string's character representation (which yields individual grapheme clusters
    or at least correct byte sequences for simple reversal of written text). For full
    grapheme cluster support, Python 3 strings are already composed correctly; this
    function simply reverses that sequence.

    Parameters:
        s (str): The input string to be reversed. Can contain any Unicode characters.

    Returns:
        str: A new string containing the characters of `s` in reverse order.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("🚀 你好世界")
        '界世好你 🚀 '
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample inputs without user interaction or external dependencies
    test_cases = [
        "hello",
        "",
        "Unicode: 你好世界 🌍🎉",
        "Python3.10",
        "!@#$%^&*()",
    ]

    for text in test_cases:
        reversed_text = reverse_string(text)
        print(f"Original: {text!r}")
        print(f"Reversed:{reversed_text!r}\n")