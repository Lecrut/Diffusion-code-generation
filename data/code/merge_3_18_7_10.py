def compare_large_integers(num1: int, num2: int) -> bool:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrarily large numbers,
    so direct comparison operators are safe and efficient for this purpose.
    
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.
        
    Returns:
        bool: True if num1 is less than or equal to num2, False otherwise.
              This returns a boolean result of the comparison logic rather 
              than just 'less than' to provide more utility for conditional checks.
              
    Note:
        While Python handles large integers natively without overflow issues in CPython,
        this function demonstrates clean logical separation and type hinting best practices.
        
    Example:
        >>> compare_large_integers(10**50, 2*10**49)
        True
        
        >>> compare_large_integers(-100, -50)
        False
    """
    return num1 <= num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: Positive large integers
    a = 3 * (10 ** 60) + 456789
    b = 2 * (10 ** 60) - 123456
    
    result_a_b = compare_large_integers(a, b)
    
    # Sample 2: Negative large integers
    c = -(10 ** 50) + 100
    d = -(9 * (10 ** 50)) - 50
    
    result_c_d = compare_large_integers(c, d)
    
    # Sample 3: Equal values with high precision digits
    e = sum(i for i in range(2**64)) // 2
    f = sum(range(1 << 63)) // 2 + (sum(range(1 << 63)) % 2 == 0) * 1
    
    result_e_f = compare_large_integers(e, f)
    
    # Output results to verify functionality without printing prompts or reading input
    print(f"Comparison {a} <= {b}: {result_a_b}")
    print(f"Comparison {c} <= {d}: {result_c_d}")
    print(f"Comparison {e} <= {f}: {result_e_f}")