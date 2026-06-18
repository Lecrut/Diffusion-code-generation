def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings efficiently using Python's built-in + operator,
    which is optimized in CPython implementations.
    
    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.
        
    Returns:
        str: A new string formed by concatenating str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    result = combine_strings(sample_str1, sample_str2)
    print(result)