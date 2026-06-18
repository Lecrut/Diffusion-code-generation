import re

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string, including those at the beginning, 
    end, or in between characters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters present.
    """
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    # Hard-coded sample multi-line strings as per requirements
    # No user input, network access, or file operations are used here
    SAMPLE_INPUT = '''Hello world! This is a test.  
  Spaces around and inside need to go completely.   
Another line with gaps.'''

    result_str = remove_all_spaces(SAMPLE_INPUT)

    print(result_str)