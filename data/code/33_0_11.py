def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.

    Args:
        text (str): The input string to process.

    Returns:
        A new string with all spaces and other whitespace removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    sample_input = "Hello, World!  This is   a test." * 2 + "\n" + "  \t\t\r\n"

    result = remove_all_spaces(sample_input)

    print(result)