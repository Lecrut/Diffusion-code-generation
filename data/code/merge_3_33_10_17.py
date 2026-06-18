def remove_all_spaces(input_str: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    This function uses a list comprehension to build a new string efficiently 
    by filtering out any character that is considered a space in Python's standard definition.
    
    Args:
        input_str (str): The input string containing potential whitespace characters.
        
    Returns:
        str: A new string with all whitespace characters removed.
    """
    return "".join(char for char in input_str if not char.isspace())

if __name__ == '__main__':
    # Sample test cases running without any user interaction or external dependencies
    samples = [
        "Hello World",           # Standard space separation
        "\t\t\n\r   Hello\tWorld  \n",  # Mixed whitespace characters
        "NoSpacesHere123!",      # String with no spaces to verify integrity
        "Multiple   Words     With   Lots   Of   Whitespace",    # Multiple consecutive spaces
        "",                      # Empty string
        " ",                     # Single space character
    ]

    for test_input in samples:
        result = remove_all_spaces(test_input)
        print(f"Input: {repr(test_input)}")
        print(f"Output: {repr(result)}\n")