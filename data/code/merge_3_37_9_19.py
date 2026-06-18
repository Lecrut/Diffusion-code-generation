def interleave_strings(str1: str, str2: str) -> str:
    """
    Interleaves two strings by concatenating the first string followed 
    by the second string as per the example provided ('hello', 'world' -> 'helloworld').
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating str1 and str2 in order.
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    s1 = "hello"
    s2 = "world"
    
    result = interleave_strings(s1, s2)
    print(result)  # Expected output: helloworld