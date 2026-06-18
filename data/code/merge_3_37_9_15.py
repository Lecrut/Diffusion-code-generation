def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings such that characters from the first string 
    appear in order followed by characters from the second string in order.
    
    This implementation simply concatenates the two strings as per the 
    example provided ('hello', 'world' -> 'helloworld'). If a more complex 
    interleaving pattern (like alternating characters) was intended, that logic 
    would need to be specified here based on typical "interleave" definitions.
    
    Given the specific instruction: "first string is followed by the second string",
    this function performs direct concatenation.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by appending str2 to str1.
    """
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = "hello"
    sample_str2 = "world"
    
    result = interleave_strings(sample_str1, sample_str2)
    print(result)