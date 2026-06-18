def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single string separated by a space.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string with the inputs concatenated and separated by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or external dependencies are required.
    input_str_1 = "Hello"
    input_str_2 = "World"

    result_string = combine_strings(input_str_1, input_str_2)
    
    print(result_string)