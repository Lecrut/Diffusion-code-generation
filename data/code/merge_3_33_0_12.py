def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters from the input string efficiently.
    
    Args:
        text (str): The input string containing potential whitespace.
        
    Returns:
        str: A new string with all whitespace removed.
    """
    return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    sample_input = "Hello, World!  This is   a test... \t\n"
    
    # Process the input using our function
    cleaned_text = remove_all_spaces(sample_input)
    
    print("Original:", repr(sample_input))
    print("Cleaned: ", repr(cleaned_text))