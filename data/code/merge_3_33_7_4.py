def skip_whitespace(s):
    """
    Generator function that yields characters from input string 
    while skipping whitespace characters (spaces, tabs, newlines).
    
    Args:
        s (str): Input string containing potentially multiple whitespaces
        
    Yields:
        str: Single character if not whitespace
    """
    for char in s:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    sample_text = "Hello  World! This is a test...      "
    
    result_list = list(skip_whitespace(sample_text))
    
    output_string = "".join(result_list)
    print(output_string)