def interleave_strings(str1: str, str2: str) -> str:
    """
    Returns a new string formed by concatenating str1 followed by str2.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
        
    Returns:
        str: A single string with the characters of str1 and str2 combined in order,
             where all characters from str1 precede those from str2.
    """
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_str1 = "hello"
    sample_str2 = "world"
    
    result = interleave_strings(sample_str1, sample_str2)
    print(result)