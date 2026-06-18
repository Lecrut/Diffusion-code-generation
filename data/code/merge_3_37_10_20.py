def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single string separated by a space.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string with the original strings concatenated and separated by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or external dependencies are required.
    sample_string_1 = "Hello"
    sample_string_2 = "World"

    result = combine_strings(sample_string_1, sample_string_2)
    
    print(result)