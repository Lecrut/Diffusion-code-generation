def compare_large_integers(num1: int, num2: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrarily large numbers,
    so direct comparison operators are safe and efficient for this purpose.
    
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.
        
    Returns:
        str: A string indicating the result of the comparison ('num1 is greater', 
             'num2 is greater', or 'both are equal').
    """
    if num1 > num2:
        return "num1 is greater"
    elif num2 > num1:
        return "num2 is greater"
    else:
        return "both are equal"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    val_a = 9007199254740993
    val_b = -6007199254740993
    
    result = compare_large_integers(val_a, val_b)
    
    # Output the comparison result.
    print(result)