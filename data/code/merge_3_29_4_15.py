def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a string, handling Unicode correctly.

    This function takes an input string containing any valid Unicode characters
    and returns a new string with the character sequence reversed. It ensures
    that multi-byte UTF-8 sequences (like emojis or accented letters) are treated
    as single units rather than being split into individual bytes.

    Parameters:
        s (str): The input string to be reversed. Can contain any Unicode characters.

    Returns:
        str: A new string with the characters of 's' in reverse order.

    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("🌍 world")  # Example with emoji and space
        "dlrow 🌍"
    """
    return s[::-1]

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python is awesome",
        "Café résumé",
        "🚀✨🎉",
        "",
        "   spaces around  "
    ]

    for test_input in sample_strings:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed:{reversed_output!r}\n")