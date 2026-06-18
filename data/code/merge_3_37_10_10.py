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
    # Hard-coded sample values to ensure the script runs without user interaction.
    input_string_1 = "Python"
    input_string_2 = "is powerful"

    result = combine_strings(input_string_1, input_string_2)
    
    print(result)