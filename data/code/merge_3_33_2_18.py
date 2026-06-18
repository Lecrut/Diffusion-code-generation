import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from both internal and external positions in the string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no space characters (' ').
    """
    return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_input = "Hello World This is a multi-line string.\nIt has spaces everywhere."

    result_string = remove_all_spaces(sample_input)

    print(result_string)