import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string, including internal 
    and surrounding ones.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no space characters (' ').
    """
    return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction)
    sample_input = "  Hello World! This is a test.   \n\n"

    result = remove_all_spaces(sample_input)
    
    print(result)