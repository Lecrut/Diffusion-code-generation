def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings efficiently using Python's optimized '+' operator 
    or f-strings depending on context. Here, simple concatenation via '+' is used 
    as it handles string joining directly and returns a new immutable string object.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: A new string formed by the concatenation of str1 and str2.
    
    Example:
        >>> combine_strings("Hello", "World")
        'HelloWorld'
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_str_1 = "Python"
    sample_str_2 = "is powerful"
    
    result = combine_strings(sample_str_1, sample_str_2)
    print(result)  # Outputs: Python is powerful