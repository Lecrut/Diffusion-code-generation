def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    This implementation uses a list comprehension to build the result efficiently,
    avoiding multiple passes over the string and minimizing intermediate object creation.

    Args:
        text (str): The input string containing potential whitespace characters.

    Returns:
        str: A new string with all whitespace characters removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "\tThis is a test\nwith multiple lines.",
        "   Leading and trailing spaces  ",
        "NoSpacesHere123!@#",
        "Mixed\tContent\r\nWithNewlines"
    ]

    for s in sample_strings:
        cleaned = remove_all_spaces(s)
        print(f"Original: {repr(s)}")
        print(f"Cleaned:  {repr(cleaned)}\n")