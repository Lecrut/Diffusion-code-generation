def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    This implementation uses a list comprehension to build a new string efficiently,
    avoiding repeated concatenation which is O(n^2). The filter function with 
    str.isspace() checks for any Unicode whitespace character as per Python standards.

    Args:
        text (str): The input string potentially containing whitespace characters.
        
    Returns:
        str: A new string with all whitespace characters removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello World",
        "\t\tNew Line\nHere",
        "   Multiple   Spaces  \nAnd Tabs ",
        "",
        "NoSpacesAtAll"
    ]

    for test_input in samples:
        result = remove_all_spaces(test_input)
        print(f'Input: {repr(test_input)}')
        print(f'Result: {repr(result)}\n')