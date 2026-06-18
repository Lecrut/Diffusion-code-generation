def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two input strings into a single string.
    
    Args:
        str1 (str): The first string argument.
        str2 (str): The second string argument.
        
    Returns:
        str: The concatenation of str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without user input
    result = combine_strings("Hello, ", "World!")
    print(result)