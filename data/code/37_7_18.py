def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings efficiently using direct concatenation.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: The concatenated result of str1 and str2 joined by a space.
    """
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    string_a = "Hello"
    string_b = "World"
    
    result = combine_strings(string_a, string_b)
    
    print(result)