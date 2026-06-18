def calculate_weight_difference(a: float, b: float) -> float:
    """
    Returns the absolute difference between two floating-point numbers.
    
    This function is optimized by using Python's built-in abs() and subtraction 
    operations which are implemented in C for maximum speed on standard platforms.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The absolute value of the difference between a and b.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 342789560.7654
    val2 = 342789560.7654
    
    result = calculate_weight_difference(val1, val2)
    
    # Output the result to verify functionality (no file I/O or network access used)
    print(f"Difference between {val1} and {val2}: {result}")

    # Additional test case with different values
    val3 = 10.5
    val4 = -7.8
    
    diff_result = calculate_weight_difference(val3, val4)
    
    print(f"Difference between {val3} and {val4}: {diff_result}")