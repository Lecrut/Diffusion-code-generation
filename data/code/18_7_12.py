def compare_large_integers(num1: int, num2: int) -> int:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python natively handles arbitrarily large integers, so direct comparison 
    is safe and efficient. This function returns a standard integer result:
        - 0 if the numbers are equal
        - 1 if num1 > num2
        - -1 if num1 < num2
    
    Args:
        num1 (int): The first large integer.
        num2 (int): The second large integer.
    
    Returns:
        int: Result of the comparison (-1, 0, or 1).
    """
    return -1 if num1 < num2 else (1 if num1 > num2 else 0)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    # Using very large integers to demonstrate handling of big numbers safely.
    
    a = int("9" * 5000)       # A number with 5000 nines
    b = int("-8" + "7" * 4999) # A negative number slightly larger than -1e+...
    
    result = compare_large_integers(a, b)
    
    print(f"Comparing: {a} vs {b}")
    if result == 0:
        print("Result: The numbers are equal.")
    elif result > 0:
        print("Result: First number is greater than the second.")
    else:
        print("Result: Second number is greater than the first.")