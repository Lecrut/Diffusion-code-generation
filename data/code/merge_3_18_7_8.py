def compare_large_integers(a: int, b: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type handles arbitrarily large numbers automatically,
    so direct comparison operators are safe and efficient for this purpose.
    
    Args:
        a (int): First integer to compare.
        b (int): Second integer to compare.
        
    Returns:
        str: 'a' if a > b, 'b' if b > a, or '=' if they are equal.
    """
    # Direct comparison is safe in Python due to arbitrary-precision integers
    return 'a' if a > b else ('b' if b > a else '=')

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: Normal positive integers
    result = compare_large_integers(5, 3)
    
    # Sample 2: Large positive integers (beyond standard 64-bit limits in other languages)
    large_a = 10**100 + 100
    large_b = 10**100
    
    result_large = compare_large_integers(large_a, large_b)
    
    # Sample 3: Negative integers
    negative_result = compare_large_integers(-50, -20)
    
    # Sample 4: Equal values (including zero and negatives)
    equal_result = compare_large_integers(0, 0)

    print(f"Comparison of {5} vs {3}: {result}")
    print(f"Comparison of large numbers ({large_a} vs {large_b}): {result_large}")