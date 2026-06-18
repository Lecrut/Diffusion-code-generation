def compare_large_integers(num1: int, num2: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrary precision,
    so standard comparison operators are safe and efficient for this purpose.
    This function simply returns the result of the comparison as a string.

    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.

    Returns:
        str: A message indicating whether num1 is less than, equal to, or greater than num2.
    """
    if num1 < num2:
        return f"{num1} is smaller than {num2}"
    elif num1 > num2:
        return f"{num1} is larger than {num2}"
    else:
        return f"{num1} is equal to {num2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    a = 9007199254740993  # A large integer near the limit of standard float precision but fits in int64
    b = -8000000000000000000000000000001  # An arbitrarily large negative number
    
    result = compare_large_integers(a, b)
    print(result)

    # Additional test case with equal values containing many digits.
    c = 123456789012345678901234567890
    d = 123456789012345678901234567890
    
    result_equal = compare_large_integers(c, d)
    print(result_equal)

    # Test case where first number is larger.
    e = 10**100 + 5
    f = 10**100 - 2
    
    result_larger = compare_large_integers(e, f)
    print(result_larger)