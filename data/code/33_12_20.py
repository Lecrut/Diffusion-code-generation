import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from both inside and surrounding areas of a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters removed from it.
    """
    return ''.join(char for char in text if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or arguments)
    SAMPLE_INPUT = "Hello World! This is a test string with   multiple    spaces  and tabs.\nAnd trailing\nspaces."

    result_string = remove_all_spaces(SAMPLE_INPUT)

    print(result_string, end='')