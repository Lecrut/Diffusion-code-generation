def interleave_strings(s1: str, s2: str) -> str:
    """
    Interleaves two strings by concatenating them in order.
    
    Note: The problem description states 'interlacing' but provides an example 
    ('hello', 'world' -> 'helloworld') which is a simple concatenation (s1 + s2),
    not true interleaving where characters from both are alternating (e.g., hwo...).
    This implementation follows the provided example and description: "first string is followed by the second".
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating s1 and s2 in that order.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    str_1 = 'hello'
    str_2 = 'world'
    
    result = interleave_strings(str_1, str_2)
    print(f"Concatenation of '{str_1}' and '{str_2}': {result}")