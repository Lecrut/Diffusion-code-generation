def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with all whitespace removed.
    """
    # Using translate for optimal performance on large strings by creating a translation table
    return text.translate(str.maketrans('', '', ' \t\n\r\f\v'))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "\t\tPython is great!\n",
        "  Multiple   spaces  and\truns. ",
        "",
        "NoSpacesHere"
    ]

    for test_input in sample_strings:
        result = remove_all_spaces(test_input)
        print(f'Input: {repr(test_input)}')
        print(f'Result: {repr(result)}\n')