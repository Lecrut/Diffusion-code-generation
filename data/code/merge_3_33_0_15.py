def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string.
    
    Args:
        text (str): The input string containing potential whitespace.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return "".join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello, World!",
        "  Python   is   great! ",
        "\t\n\t\n",
        "No spaces here",
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f"Input: {repr(sample)}")
        print(f"Output: {repr(result)}\n")