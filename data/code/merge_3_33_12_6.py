import re

def strip_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string, including internal and surrounding ones.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters of type ' '.
    """
    # Use regular expression or direct replacement to remove only space characters (' ')
    return re.sub(r'\s', '', text)

if __name__ == '__main__':
    sample_input = "  Hello World! This is a test.   \n\n\tSpaces everywhere."
    
    processed_output = strip_all_spaces(sample_input)
    
    # Print the result directly to stdout using f-string for clarity and efficiency
    print(processed_output)