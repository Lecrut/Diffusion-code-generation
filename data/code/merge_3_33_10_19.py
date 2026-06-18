def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string.
    
    This function uses a list comprehension to build a new string efficiently by iterating
    over each character and including it only if it is not a whitespace character.
    The join method is then used for optimal performance in constructing the final string.

    Args:
        text (str): The input string containing potential whitespace characters.

    Returns:
        str: A new string with all whitespace characters removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    sample_1 = "Hello World\nThis is a test\twith spaces."
    sample_2 = "\t\n\r   \n  "
    
    result_1 = remove_all_spaces(sample_1)
    result_2 = remove_all_spaces(sample_2)

    print(f"Input: {repr(sample_1)}")
    print(f"Output: {result_1}")
    print()
    print(f"Input: {repr(sample_2)}")
    print(f"Output: '{result_2}'")