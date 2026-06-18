def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings into a single string efficiently using Python's native behavior.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str_1 = "Hello, "
    sample_str_2 = "World!"
    result = combine_strings(sample_str_1, sample_str_2)
    print(result)