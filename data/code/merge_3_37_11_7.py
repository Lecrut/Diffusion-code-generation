def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings into a new string using Python's most efficient 
    built-in operator which is optimized in CPython implementation.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating str1 and str2.
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external inputs
    sample_1 = "Hello"
    sample_2 = "World!"

    result = combine_strings(sample_1, sample_2)
    
    print(result)