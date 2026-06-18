def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single concatenated string.
    
    Args:
        str1 (str): The first string argument.
        str2 (str): The second string argument.
        
    Returns:
        str: The concatenation of the two strings in order (str1 + str2).
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    first_string = "Hello"
    second_string = "World!"
    
    result = combine_strings(first_string, second_string)
    print(result)