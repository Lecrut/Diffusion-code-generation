def interleave_strings(s1: str, s2: str) -> str:
    """
    Concatenates two strings where s1 is followed by s2.
    
    Args:
        s1 (str): The first string to be interleaved.
        s2 (str): The second string to be interleaved after the first.
        
    Returns:
        str: A new string formed by concatenating s1 and s2 in order.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    result = interleave_strings("hello", "world")
    print(result)  # Expected output: helloworld