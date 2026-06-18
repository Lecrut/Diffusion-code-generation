import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string, both internal (between words/characters)
    and external (leading/trailing).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no space characters (' ').
    """
    return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    SAMPLE_INPUT = "Hello World This is a test string with multiple spaces.   And some trailing ones."

    # Simulate reading from standard input using the hard-coded value directly
    # to ensure no file I/O errors occur since we are not writing/reading actual files.
    if isinstance(SAMPLE_INPUT, str):
        result = remove_all_spaces(SAMPLE_INPUT)
        print(result)
    else:
        raise TypeError("SAMPLE_INPUT must be a string.")