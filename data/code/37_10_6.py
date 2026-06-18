def combine_strings(string1: str, string2: str) -> str:
    """
    Combines two input strings with a single space separator.
    
    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.
        
    Returns:
        str: A new string formed by joining the inputs with a space.
    """
    return f"{string1} {string2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user interaction, arguments, or network access.
    sample_string_1 = "Hello"
    sample_string_2 = "World"

    result = combine_strings(sample_string_1, sample_string_2)
    
    print(result)