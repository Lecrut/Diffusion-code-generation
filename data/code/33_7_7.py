def remove_whitespace_generator(s: str):
    """
    Generator function that yields characters from an input string 
    excluding whitespace (spaces, tabs, newlines).
    
    Args:
        s (str): Input string to process
        
    Yields:
        str: Individual non-whitespace characters
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_string = "Hello World! This is a test."
    
    print("Original string:")
    print(test_string)
    print("\nFiltered characters (no whitespace):")
    
    result_list = list(remove_whitespace_generator(test_string))
    filtered_str = "".join(result_list)
    print(filtered_str)