def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings efficiently. For simple concatenation of 
    scalars, direct addition is optimal and avoids overhead of .join().
    
    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.
        
    Returns:
        str: A new string resulting from the combination.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    s_a = "Hello"
    s_b = "World!"
    
    result = combine_strings(s_a, s_b)
    print(result)  # Expected output: HelloWorld!