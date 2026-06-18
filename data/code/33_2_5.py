import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from both internal and external positions in the string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    return ''.join(char for char in text if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    sample_input = "Hello World\nThis is a test.\n  Leading and trailing spaces."

    output_string = remove_all_spaces(sample_input)
    
    print(output_string)