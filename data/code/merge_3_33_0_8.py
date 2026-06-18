def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.
    
    Args:
        text (str): The input string containing potential whitespace.
        
    Returns:
        str: A new string with all whitespace removed.
    """
    return ''.join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello, World!",
        "  Multiple   Spaces  ",
        "\tNewlines\nand\rCarriageReturns",
        "NoSpacesHere123"
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f'Input: {repr(sample)}')
        print(f'Output: {repr(result)}\n')