def remove_whitespace_generator(text: str):
    """
    Generator function that yields characters from an input string,
    skipping any whitespace characters (spaces, tabs, newlines).
    
    Args:
        text (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters one at a time.
    """
    for char in text:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_string = "Hello World! This is a test."

    print("Original string:")
    print(sample_string)
    
    print("\nFiltered characters (spaces removed):")
    filtered_chars = list(remove_whitespace_generator(sample_string))
    result_str = "".join(filtered_chars)
    print(result_str)