def combine_strings(a: str, b: str) -> str:
    """
    Combines two strings efficiently using direct concatenation.
    
    Args:
        a (str): The first string to combine.
        b (str): The second string to combine.
        
    Returns:
        str: A new string containing both input strings concatenated.
    """
    return a + b

if __name__ == '__main__':
    # Sample values without user interaction or file access
    sample_string_1 = "Hello"
    sample_string_2 = ", World!"
    
    result = combine_strings(sample_string_1, sample_string_2)
    print(result)