def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function takes a string input and returns a new string with its characters
    in reversed order. It properly handles all Unicode characters including emojis 
    by iterating over code points rather than bytes or characters as interpreted by some languages.

    Parameters:
        s (str): The input string to be reversed. Can contain any valid Unicode characters.

    Returns:
        str: A new string containing the characters of 's' in reverse order.

    Example:
        >>> reverse_string("Hello, 世界")
        "界世，olleH"
        >>> reverse_string("🌍💡✨")
        "✨💡🌍"
    """
    return "".join(char for char in s[::-1])

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_1 = "Hello, World!"
    sample_2 = "Unicode: \u039d\u0178 (Greek letters)"
    sample_3 = "\ud83c\udf0d🌍💡✨"  # Emojis

    print(f"Original ({sample_1!r}): {reverse_string(sample_1)}")
    print(f"Original ({sample_2!r}): {reverse_string(sample_2)}")
    print(f"Original ({sample_3!r}): {reverse_string(sample_3)}")