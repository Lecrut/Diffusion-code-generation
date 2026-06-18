def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings efficiently.
    
    For simple concatenation of two strings, direct addition is optimal in Python
    as it involves minimal overhead compared to list-based approaches with join().
    
    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.
        
    Returns:
        str: A new string formed by concatenating str1 and str2 in that order.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str_1 = "Hello"
    sample_str_2 = ", World!"
    
    result = combine_strings(sample_str_1, sample_str_2)
    print(result)  # Output: Hello, World!