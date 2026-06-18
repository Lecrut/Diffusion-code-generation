def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single string separated by a space.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string containing both inputs separated by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, or network access.
    sample_str1 = "Hello"
    sample_str2 = "World"
    
    result_string = combine_strings(sample_str1, sample_str2)
    print(result_string)