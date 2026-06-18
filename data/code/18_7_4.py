def compare_large_integers(num1: int, num2: int) -> tuple[int, str]:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrary precision,
    so standard comparison operators are safe and efficient for this purpose.
    This function simply returns the result of a direct comparison as both
    an exit code (0 if equal, 1 if num2 > num1, -1 otherwise) 
    and a descriptive string message for clarity.

    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.

    Returns:
        tuple[int, str]: A tuple containing the comparison result code 
                        and a human-readable description of the relationship between the numbers.
    
    Examples:
        >>> compare_large_integers(10, 5)
        (-1, 'num2 is greater than num1')
        
        >>> compare_large_integers(-5, -3)
        (1, 'num2 is greater than num1')
        
        >>> compare_large_integers(429496729850L, 429496729850)
        (0, 'numbers are equal')
    """
    # Direct comparison using Python's arbitrary precision integers is safe.
    if num1 == num2:
        return 0, "Numbers are equal"
    
    if num1 < num2:
        return -1, f"{num1} is less than {num2}"
    else:
        return 1, f"{num1} is greater than {num2}"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    # These include standard integers and potentially large numbers 
    # (though Python handles them natively).
    
    a = 10**50 + 34829            # Large positive integer
    b = -10**60                   # Negative number with larger magnitude
    
    result_code, message = compare_large_integers(a, b)
    
    print(f"Comparing {a} and {b}")
    print(f"Result Code: {result_code}")
    print(f"Description: {message}")

    # Additional test case for equality
    c = 12345678901234567890
    
    result_eq, msg_eq = compare_large_integers(c, c)
    
    if __name__ == '__main__':
        print(f"\nEquality Test: {c} vs {c}")
        print(f"Result Code: {result_eq}")
        print(f"Description: {msg_eq}")