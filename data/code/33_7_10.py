import sys

def filter_whitespace(s: str):
    """
    Generator function that yields characters from input string s,
    skipping any whitespace characters (spaces, tabs, newlines).
    
    Args:
        s (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters from the input string.
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    test_string = "Hello, World!  This is a test."
    
    print("Original string:")
    print(test_string)
    print("\nFiltered characters:")
    
    for char in filter_whitespace(test_string):
        sys.stdout.write(char)
        
    # Ensure the output ends with a newline for clean printing
    if not test_string[-1].isspace():
        sys.stdout.write('\n')