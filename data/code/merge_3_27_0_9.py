def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different from each other, False otherwise.
    
    This function uses a direct comparison which is highly optimized in Python's C implementation.
    It handles integers and floating-point numbers correctly. For floats, it treats them as 
    equal only if they have the exact same bit representation (not considering epsilon for equality),
    unless specific tolerance logic was requested, but standard 'different' implies inequality.

    Args:
        a (float): The first numerical value.
        b (float): The second numerical value.

    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    val1 = 5.0
    val2 = 7
    
    result = check_difference(val1, val2)
    
    if result:
        print("The numbers are different.")
    else:
        print("The numbers are equal.")