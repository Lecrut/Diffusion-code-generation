def interleave_strings(s1: str, s2: str) -> str:
    """
    Returns a new string formed by concatenating s1 followed by s2.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: A single string combining the characters of both inputs in order, 
             where all characters from s1 precede those from s2.
    
    Example:
        >>> interleave_strings('hello', 'world')
        'helloworld'
    """
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    str_one = "hello"
    str_two = "world"
    
    result_string = interleave_strings(str_one, str_two)
    
    print(result_string)