def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.

    Args:
        text (str): The input string containing potential whitespace.

    Returns:
        str: A new string with no whitespace characters removed, or an empty string if none exist.
    """
    return "".join(text.split())

if __name__ == "__main__":
    # Sample test cases run without user interaction
    samples = [
        "Hello World",
        "  Multiple   Spaces  ",
        "\t\n\tNewlines and tabs",
        "NoSpacesHere123!",
        "",
        " \t\n\r\u00a0\xa0\u2009\u2060"
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f'Input: {repr(sample)}')
        print(f'Output: {result}')