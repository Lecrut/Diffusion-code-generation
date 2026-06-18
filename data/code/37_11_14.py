def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings efficiently using Python's optimized string join method.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating the arguments.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World!"
    
    result = combine_strings(sample_str1, sample_str2)
    print(result)