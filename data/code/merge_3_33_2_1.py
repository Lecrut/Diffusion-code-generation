import sys

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string, including both internal 
    and external whitespace characters (spaces).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no space characters remaining.
    """
    return ''.join(char for char in text if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_input = "Hello World\nThis is a test.\n  Spaces everywhere!  \n"

    # Simulate reading from standard input by using the hard-coded string directly.
    # In a real scenario with file I/O best practices for stdin redirection:
    #   sys.stdin.read() would be used, but here we use the variable to ensure 
    #   no interactive prompts or external dependencies are triggered.

    result = remove_all_spaces(sample_input)

    print(result)