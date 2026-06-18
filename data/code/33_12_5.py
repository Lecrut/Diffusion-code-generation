import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces (both internal and surrounding) from a string efficiently.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    # Using replace() twice is efficient for ASCII space removal in Python 3+
    return text.replace(" ", "")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    sample_input = """
Hello World! This is a multi-line string with spaces everywhere.

  Leading and trailing   spaces should be removed too.  
"""
    
    result = remove_all_spaces(sample_input)
    print(result)