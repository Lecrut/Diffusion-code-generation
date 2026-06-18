import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from both internal and surrounding positions in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters removed.
    """
    return "".join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # This ensures the script runs without user input or network access.
    SAMPLE_INPUT = "Hello, World!   \n  Python   is   great."

    result_str: str = remove_all_spaces(SAMPLE_INPUT)
    
    print(result_str)