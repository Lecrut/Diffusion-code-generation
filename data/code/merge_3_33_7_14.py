def filter_non_whitespace(s: str):
    """
    Generator function that yields characters from an input string 
    excluding whitespace characters (spaces, tabs, newlines).
    
    Args:
        s (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters from the input.
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    test_string = "Hello World! This is a Python script."
    
    print("Original string:")
    print(test_string)
    print("\nFiltered characters (spaces removed):")
    
    result_list = list(filter_non_whitespace(test_string))
    filtered_str = "".join(result_list)
    print(filtered_str)