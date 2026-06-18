def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.
    
    Args:
        text (str): The input string containing potential whitespace.
        
    Returns:
        str: A new string with all leading, trailing, and middle 
             spaces removed using built-in strip() method which handles 
             various unicode whitespace correctly in modern Python 3.x.
    """
    return ''.join(text.split())

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "\t\n   \n\tFinal Text\n ",
        "NoSpacesHere!!!",
        "  Leading and Trailing Spaces  ",
        "Mixed\tTabs,\nNewlines, and spaces"
    ]
    
    for original in sample_strings:
        result = remove_all_spaces(original)
        print(f"Input:     {repr(original)}")
        print(f"Output:    {repr(result)}")
        print("-" * 40)