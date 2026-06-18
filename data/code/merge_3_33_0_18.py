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
    # Sample test cases running without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "  Multiple   spaces  and\ttabs\nnewlines ",
        "NoSpacesHere",
        "\t \n\r\f\v",
        "Mixed: \t spaced\tnormally"
    ]

    for sample in samples:
        print(f"Input: {repr(sample)}")
        result = remove_all_spaces(sample)
        print(f"Output: {repr(result)}")
        print("-" * 40)