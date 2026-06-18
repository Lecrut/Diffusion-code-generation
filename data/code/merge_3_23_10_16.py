import math

def are_floats_equal(value1: float, value2: float, tolerance: float) -> bool:
    """
    Compares two floating-point numbers for equality within a specified absolute tolerance.

    Args:
        value1 (float): The first number to compare.
        value2 (float): The second number to compare.
        tolerance (float): The maximum allowed difference between the values. Must be non-negative.

    Returns:
        bool: True if |value1 - value2| <= tolerance, False otherwise.

    Note:
        This method uses absolute differences rather than relative comparisons
        which can lead to unexpected behavior for very small numbers near zero.
    """
    if tolerance < 0:
        raise ValueError("Tolerance must be non-negative.")
    
    return abs(value1 - value2) <= tolerance

if __name__ == '__main__':
    # Sample test cases executed without any external input or dependencies
    
    # Test Case 1: Numbers very close but not exactly equal (within typical float precision limits for exact equality checks)
    num_a = 0.1 + 0.2
    num_b = 0.3
    is_exact_equal = num_a == num_b
    print(f"Test 1 - Exact Equality Check:")
    print(f"  Value A: {num_a:.20f}")
    print(f"  Value B: {num_b:.20f}")
    print(f"  Are they exactly equal? {is_exact_equal}\n")

    # Test Case 2: Numbers within a standard tolerance (e.g., machine epsilon or user-defined small value)
    num_c = 1.0 / 3.0
    num_d = round(1/3, 5)
    tolerance_1 = 1e-9
    
    print(f"Test 2 - Tolerance Check:")
    print(f"  Value C: {num_c}")
    print(f"  Rounded D (precision 5): {num_d}")
    result_tolerant = are_floats_equal(num_c, num_d, tolerance_1)
    print(f"  Difference <= {tolerance_1}? {result_tolerant}\n")

    # Test Case 3: Negative numbers comparison
    neg_a = -0.5 + 1e-6
    neg_b = -0.4999995
    tolerance_neg = 1e-7
    
    print(f"Test 3 - Negative Numbers with Tight Tolerance:")
    result_neg_tight = are_floats_equal(neg_a, neg_b, tolerance_neg)
    print(f"  {neg_a:.6f} == {neg_b:.6f}? (tight tol: {tolerance_neg}) -> {result_neg_tight}\n")

    # Test Case 4: Large numbers comparison using absolute difference might fail if relative error is expected,
    # but this demonstrates the use of Math for handling potential overflow in subtraction logic 
    # by relying on the robust properties of floating point representation where applicable.
    large_num_1 = 1e20 + 50
    large_num_2 = 1e20 + 49
    
    print(f"Test 4 - Large Number Comparison (Absolute Tolerance):")
    # Note: In standard IEEE 754 doubles, the gap between integers at this magnitude is > 1.
    abs_diff_large = abs(large_num_1 - large_num_2)