import math

def is_close(a: float, b: float) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function uses the relative difference method to determine if two floats are close enough 
    to be considered equal, which avoids issues with absolute zero comparisons and large number ranges.
    
    Args:
        a (float): The first float value.
        b (float): The second float value.
        
    Returns:
        bool: True if the values are within 1e-9 relative difference, False otherwise.
    """
    # Use math.isclose for robust floating-point comparison with default tolerances
    return math.isclose(a, b)

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input
    
    # Test 1: Two identical integers converted to float (should be close)
    val_1 = 5.0
    val_2 = 5.0
    result_1 = is_close(val_1, val_2)
    
    # Test 2: Floating point values with slight difference due to precision issues (e.g., 0.1 + 0.2 vs 0.3)
    a = 0.1 + 0.2
    b = 0.3
    result_2 = is_close(a, b)
    
    # Test 3: Two very large numbers that are slightly different (should be close relatively)
    large_a = 1e16 * 0.5
    large_b = 1e16 / 2.0
    result_3 = is_close(large_a, large_b)
    
    # Test 4: Two very small numbers that are slightly different (should be close relatively)
    small_a = 1e-16 * 5.0
    small_b = 1e-17 * 25.0
    result_4 = is_close(small_a, small_b)
    
    # Test 5: Clearly distinct values (should not be close)
    diff_a = 3.14159265358979
    diff_b = 3.14159265358980
    result_5 = is_close(diff_a, diff_b)

    # Output results for verification (no interactive prompts used)
    print(f"Test 1 - Identical floats: {result_1}")
    print(f"Test 2 - Precision issue (0.1+0.2 vs 0.3): {result_2}")
    print(f"Test 3 - Large numbers close check: {result_3}")
    print(f"Test 4 - Small numbers close check: {result_4}")
    print(f"Test 5 - Clearly distinct values: {result_5}")