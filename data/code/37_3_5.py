def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two input strings using the '+' operator.
    
    Args:
        s1 (str): The first string to be concatenated.
        s2 (str): The second string to be concatenated.
        
    Returns:
        str: A new string formed by concatenating s1 and s2.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    str_a = "Hello"
    str_b = "World!"

    result = combine_strings(str_a, str_b)
    
    print(f"Result: '{result}'")