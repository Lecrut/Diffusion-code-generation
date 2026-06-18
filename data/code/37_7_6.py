def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings efficiently using direct concatenation.
    
    Args:
        str1 (str): The first string to be combined.
        str2 (str): The second string to be combined.
        
    Returns:
        str: The concatenated result of the two input strings.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    sample_str_1 = "Hello"
    sample_str_2 = "World"
    
    combined_result = combine_strings(sample_str_1, sample_str_2)
    print(combined_result)  # Output: HelloWorld