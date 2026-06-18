import sys

def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings by concatenating them in order with a space separator.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: The combined result of s1 and s2 separated by a single space.
    """
    return f"{s1} {s2}"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement for no user input, args, or network access.
    str_a = "Hello"
    str_b = "World"
    
    result = combine_strings(str_a, str_b)
    print(result)