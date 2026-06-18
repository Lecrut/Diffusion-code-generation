def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings with a space in between using direct concatenation 
    for optimal performance in this simple case.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: The concatenated result of the two strings separated by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    string_a = "Hello"
    string_b = "World"
    
    result = combine_strings(string_a, string_b)
    print(result)  # Output: Hello World