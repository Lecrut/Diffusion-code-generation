def compare_integers(a: int, b: int) -> str:
    """
    Compares two integers and returns a string indicating their relationship.
    
    Args:
        a (int): The first integer to be compared.
        b (int): The second integer to be compared.
        
    Returns:
        str: "a is less than b", "a equals b", or "a is greater than b"
    """
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} equals {b}"

if __name__ == '__main__':
    pass
