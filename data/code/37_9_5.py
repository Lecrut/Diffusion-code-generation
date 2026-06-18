def interleave_strings(str1: str, str2: str) -> str:
    """
    Returns a new string formed by concatenating str1 followed by str2.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A combined string where the characters of str1 appear 
             in order, immediately followed by the characters of str2 
             in order. This is equivalent to standard concatenation.
    
    Example:
        'hello', 'world' -> 'helloworld'
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    s1 = "hello"
    s2 = "world"
    
    result = interleave_strings(s1, s2)
    
    print(result)