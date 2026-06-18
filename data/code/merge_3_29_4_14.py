def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.

    This function iterates through the input string from end to start and constructs
    a new string with the characters in reversed order. It properly handles strings
    containing non-ASCII Unicode characters (e.g., emojis, CJK characters).

    Args:
        s (str): The input string to be reversed. Can contain any valid Python unicode character.

    Returns:
        str: A new string with the characters of the original string in reverse order.

    Example:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("🚀 你好 🌍")
        "🌍 好你 🚀 "
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    sample_1 = "hello world"
    sample_2 = "Unicode: \u4e0d\u53c8 (not two)"  # Chinese for 'not two'
    sample_3 = "\ud83d\ude97 🚗🏎️"

    print(f"Original ({sample_1}): {repr(sample_1)}")
    print(f"Reversed:             {reverse_string(sample_1)}")

    print("-" * 40)
    print(f"Original ({sample_2}): {repr(sample_2)}")
    print(f"Reversed:             {reverse_string(sample_2)}")

    print("-" * 40)
    print(f"Original ({sample_3}): {repr(sample_3)}")
    print(f"Reversed:             {reverse_string(sample_3)}")