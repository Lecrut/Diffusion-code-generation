def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single string separated by a space.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string with the inputs concatenated and separated by ' '.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction is required
    input_string_a = "Python"
    input_string_b = "Programming"

    result = combine_strings(input_string_a, input_string_b)

    print(result)