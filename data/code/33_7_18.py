def remove_whitespace_generator(text):
    """
    Generator function that yields characters from input string excluding whitespace.
    
    Args:
        text (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters one at a time.
    """
    for char in text:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    sample_string = "Hello, World! This is an example."
    
    # Convert generator to list for demonstration purposes during execution
    result_list = []
    count = 0
    
    print("Processing:", repr(sample_string))