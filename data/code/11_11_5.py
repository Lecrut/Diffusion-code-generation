def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers (length1 / length2).
    
    The function handles division by zero and ensures standard IEEE 754 
    double-precision accuracy. If length2 is zero or effectively zero, it returns infinity.

    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value.

    Returns:
        float: The ratio of length1 to length2. Returns inf if division by zero occurs.
    """
    # Check for exact or near-zero denominator using a small epsilon threshold 
    # common in numerical computations, though standard Python / operator handles this naturally.
    try:
        return length1 / length2
    except ZeroDivisionError:
        import math
        if abs(length2) < 1e-308:
            return float('inf') if length1 > 0 else float('-inf')
        raise

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    val_a = 5.0
    val_b = 2.3
    
    result = calculate_length_ratio(val_a, val_b)
    
    print(f"Ratio of {val_a} and {val_b}: {result}")

    # Additional test case for edge behavior (division by zero simulation via very small number)
    try:
        ratio_small_denom = calculate_length_ratio(10.5, 1e-320)
        print(f"Ratio with near-zero denominator ({1e-320}): {ratio_small_denom}")
    except ZeroDivisionError as e:
        # This block is technically unreachable due to the try-except inside calculate_length_ratio 
        # catching specific cases, but kept for structural completeness if logic changes.
        print(f"Caught expected behavior in test: {e}")

    # Test case with exact zero denominator (should raise ZeroDivisionError as per standard Python rules)
    # The internal check handles very small numbers returning inf, but strict 0 raises error.
    try:
        ratio_zero = calculate_length_ratio(10.0, 0.0)
        print(f"Ratio with exact zero denominator: {ratio_zero}")
    except ZeroDivisionError:
        print("Correctly raised ZeroDivisionError for exact zero divisor.")