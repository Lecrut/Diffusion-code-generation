def remove_whitespace_generator(s: str):
    """
    Generator function that yields characters from input string s,
    excluding any whitespace characters (spaces, tabs, newlines).
    
    Args:
        s (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters from the input string.
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    test_string = "Hello World! This is a Python generator."
    
    print("Original string:")
    print(test_string)
    print("\nFiltered characters (spaces removed):")
    
    for char in remove_whitespace_generator(test_string):
        print(char, end='')