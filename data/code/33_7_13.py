def filter_non_whitespace(s: str):
    """
    Generator function that yields characters from an input string 
    excluding whitespace (spaces, tabs, newlines).
    
    Args:
        s (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters from the input.
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    test_string = "Hello World! This is a test."
    
    print("Original string:", repr(test_string))
    result_list = list(filter_non_whitespace(test_string))
    cleaned_string = "".join(result_list)
    print("Filtered characters:", result_list)
    print("Resulting string without spaces:", repr(cleaned_string))