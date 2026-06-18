def compare_large_integers(num1: int, num2: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrarily large numbers,
    so standard comparison operators are safe and efficient for this purpose.
    This function simply returns a string indicating the relationship between 
    num1 and num2 to demonstrate clean logic handling of large values.

    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.

    Returns:
        str: A description of the comparison result ('num1 is greater', 
             'num1 is less', or 'numbers are equal').
    """
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2:
        return f"{num1} is less than {num2}"
    else:
        return "The numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values including potentially large integers.
    # These do not require user input, command-line arguments, or network access.
    val_a = 10**50 + 342
    val_b = -987654321
    
    result = compare_large_integers(val_a, val_b)
    
    print(result)