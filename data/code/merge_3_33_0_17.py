def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.
    
    Args:
        text (str): The input string containing potential whitespace.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return ''.join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user interaction
    samples = [
        "Hello, World!",
        "  Multiple   Spaces  ",
        "\t\n\tNewlines and tabs",
        "No spaces here",
        "1234567890"
    ]

    for sample in samples:
        result = remove_all_spaces(sample)
        print(f"Input: {repr(sample)}")
        print(f"Output: {result}")
        print("-" * 20)