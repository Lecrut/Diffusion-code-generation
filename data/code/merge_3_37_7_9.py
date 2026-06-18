def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings into a single string directly.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: The combined result of appending s2 to s1.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_1 = "Hello"
    sample_2 = "World!"
    
    result = combine_strings(sample_1, sample_2)
    print(result)