def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two input strings into a single string.
    
    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.
        
    Returns:
        str: A new string that is the concatenation of str1 and str2.
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    result = combine_strings("Hello", "World")
    print(result)