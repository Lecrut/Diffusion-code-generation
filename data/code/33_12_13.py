import re

def clean_string(text: str) -> str:
    """
    Removes all spaces from both internal positions and surrounding edges of the string.
    
    Args:
        text (str): The input multi-line string to be processed.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction or files needed)
    sample_input = "  Hello World! This is a multi-line string.\nIt has extra spaces here   and there. -> NO SPACES"
    
    result_string = clean_string(sample_input)
    
    print(result_string)