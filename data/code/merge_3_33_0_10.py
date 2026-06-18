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
    # Hard-coded sample values to test the function without user interaction
    samples = [
        "Hello, World!",
        "  Python   is   great! ",
        "\t\n\t\n",
        "No spaces here"
    ]

    for s in samples:
        result = remove_all_spaces(s)
        print(f'Original: {repr(s)}')
        print(f'Result:   {repr(result)}\n')