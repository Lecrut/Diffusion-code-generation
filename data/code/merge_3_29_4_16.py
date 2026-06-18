def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates over the input string and constructs a new string with 
    characters added in reverse order. It properly handles all Unicode code points, 
    including those that may be composed or decomposed forms (e.g., accented letters).
    
    Parameters:
        s (str): The input string to be reversed.

    Returns:
        str: A new string with the characters of the original string in reverse order.

    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("你好世界")
        '界世好你'
        >>> reverse_string("café")
        'éfac'
    """
    return "".join(reversed(s))

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_strings = [
        "hello",
        "你好世界",
        "café",
        "",
        "Unicode: \u0435\u0421\u0422\u0418 (Russian)",
        "\ud83c\udf09"  # Grinning Sun emoji
    ]

    for test_str in sample_strings:
        reversed_result = reverse_string(test_str)
        print(f"Original: {test_str!r}")
        print(f"Reversed:{reversed_result!r}\n")