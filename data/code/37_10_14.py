def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two input strings into a single string separated by a space.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string containing both inputs concatenated with a space in between.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to ensure no interactive prompts or external dependencies are needed.
    first_string = "Hello"
    second_string = "World"
    
    result = combine_strings(first_string, second_string)
    print(result)