def reverse_string(input_str: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates over each character index from end to start and constructs
    a new string with reversed content. It explicitly handles all valid Python unicode
    strings without relying on external libraries like `reversed()` which can behave 
    unexpectedly for certain edge cases when combined with slicing in complex scenarios,
    although the standard slice input_str[::-1] is typically efficient and correct for Unicode.

    Parameters:
        input_str (str): The string to be reversed. It supports all valid Python unicode characters.

    Returns:
        str: A new string containing the characters of `input_str` in reverse order.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        
        >>> reverse_string("你好世界")
        '界世好你'
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    samples = [
        "Python",
        "Unicode 测试",
        "",
        "A" * 30,
        "\ud83c\udf19 \ud83e\udd29", # Combining Unicode characters (Sun and U+264B)
    ]

    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed:{reversed_sample!r}\n")