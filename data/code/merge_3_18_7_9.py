def compare_large_integers(a: int, b: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrarily large numbers,
    so direct comparison operators are safe and efficient for this task.
    
    Args:
        a (int): First integer value.
        b (int): Second integer value.
        
    Returns:
        str: 'greater' if a > b, 'less' if a < b, or 'equal' if a == b.
    """
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    val1 = 9007199254740993 ** 2  # A very large positive integer (approx 8 * 10^36)
    val2 = -9007199254740993      # A negative counterpart to test sign handling
    
    result_a_b = compare_large_integers(val1, val2)
    
    sample_equal_1 = (10**18 + 5)**2
    sample_equal_2 = (10**18 + 6)*(10**18 + 4) # This product equals the square above
    
    result_eq_test = compare_large_integers(sample_equal_1, sample_equal_2)
    
    print(f"Comparison of {val1} and {val2}: '{result_a_b}'")
    print(f"Verification test (should be equal): '{result_eq_test}'")