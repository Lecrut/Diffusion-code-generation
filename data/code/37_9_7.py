def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings by concatenating characters from each in order.
    
    This function takes two input strings and returns a new string where 
    the first string is followed immediately by the second string.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A single string formed by concatenating str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_str1 = 'hello'
    sample_str2 = 'world'
    
    result = interleave_strings(sample_str1, sample_str2)
    print(result)  # Expected output: helloworld