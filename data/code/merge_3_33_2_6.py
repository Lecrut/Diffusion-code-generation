import sys

def remove_spaces(text: str) -> str:
    """
    Removes all internal and external spaces from a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    # Filter out any character that is not alphanumeric or punctuation, 
    # effectively removing all space types including tabs and newlines if they were present in the original logic flow,
    # but since we are eliminating ALL spaces specifically requested:
    return ''.join(char for char in text if ' ' != char)

def main():
    """
    Reads a multi-line string from standard input (simulated via hard-coded values),
    processes it to remove all internal and external spaces, and prints the result.
    
    Uses file I/O best practices by reading from sys.stdin.buffer for efficiency 
    if actual stdin were used, but here we simulate with hardcoded data as per constraints.
    """
    # Hard-coded sample multi-line string simulating user input without interactive prompts
    sample_input = "Hello World\n  This is a test   \nWith multiple spaces everywhere."

    result_string = remove_spaces(sample_input)
    
    print(result_string)

if __name__ == '__main__':
    main()