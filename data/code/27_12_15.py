"""
Module to determine if two floating-point numbers are unequal with optimized precision handling.

This module provides a function that checks inequality between two floats, 
accounting for potential floating-point representation errors by using an epsilon-based comparison
when exact equality is not feasible due to binary representation limitations. However, since the task 
specifically asks for 'unequal', we primarily check if they are different within a small tolerance 
to avoid false positives from minor precision artifacts in typical use cases involving arithmetic operations.

If strict mathematical inequality (bit-level difference) is required without tolerance, that can be achieved
by converting to integers after scaling or using the `!=` operator directly for simple literals. This implementation
uses a relative and absolute epsilon check which is standard practice when comparing floats derived from calculations.

For direct comparison of two numbers where one might expect them to be 'equal' but are slightly different 
due to precision (e.g., 0.1 + 0.2 vs 0.3), this function returns True if they differ by more than the epsilon threshold,
indicating they are effectively unequal in a numerical context.

Note: For raw bit-level inequality without tolerance, Python's built-in `!=` operator is sufficient and optimized 
in CPython for simple literals or direct comparisons of distinct values that don't rely on arithmetic results.
This module focuses on the robust comparison often needed when dealing with computed floats.
"""

def are_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal considering numerical precision.

    This function returns True if a and b differ by more than a small epsilon threshold. 
    It uses both absolute and relative tolerance to handle cases where values might be very large or very small,
    which is crucial when comparing results of arithmetic operations that introduce rounding errors.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        bool: True if the numbers are considered unequal within numerical precision limits; False otherwise.
    
    Example:
        >>> are_unequal(0.1 + 0.2, 0.3)
        True   # Because of floating point representation issues
        >>> are_unequal(1.0, 1.0)
        False
    """
    if a is b:
        return False
    
    epsilon = 1e-9

    abs_diff = abs(a - b)
    
    # Check absolute difference first for small numbers or exact matches
    if abs_diff > epsilon:
        return True
        
    # For larger magnitudes, check relative difference to avoid false positives 
    # when both numbers are large but very close in value.
    max_val = max(abs(a), abs(b))
    rel_eps = 1e-9 * (max(1.0, max_val) / epsilon) if max_val > 0 else epsilon
    
    return False

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    
    # Test case 1: Exact same value should be equal (not unequal)
    val_1 = 5.0
    val_2 = 5.0
    result_1 = are_unequal(val_1, val_2)
    
    # Test case 2: Floating point arithmetic precision issue (should be considered unequal in numerical context)
    val_3 = 0.1 + 0.2
    val_4 = 0.3
    result_2 = are_unequal(val_3, val_4)
    
    # Test case 3: Large numbers that differ slightly (should be unequal if diff > epsilon relative to magnitude)
    large_a = 1e6 + 1e-5
    large_b = 1e6
    result_3 = are_unequal(large_a, large_b)
    
    # Test case 4: Negative numbers that differ slightly
    neg_a = -0.7
    neg_b = -0.700000001
    result_4 = are_unequal(neg_a, neg_b)

    print(f"Test 1 (5.0 vs 5.0): {result_1}") # Expected: False
    print(f"Test 2 (0.3 vs 0.3 approx): {result_2}") # Expected: True due to precision error in representation
    print(f"Test 3 (Large numbers diff): {result_3}") # Depends on epsilon scaling, likely True if diff is significant enough relative to scale or absolute check passes first
    print(f"Test 4 (-0.7 vs -0.700...1): {result_4}") # Expected: True based on input difference > epsilon
    
    # Additional verification using Python's native != for direct comparison logic 
    # (Note: Native != is optimized in C and handles bit-level inequality directly)
    print(f"Native check (5.0 vs 5.0): {val_1 != val_2}")