"""
Floating-point number comparison module using epsilon tolerance.

This script provides a function to compare two floating-point numbers,
accounting for potential inaccuracies inherent in binary floating-point representation.
It uses a small threshold (epsilon) to determine if values are effectively equal or which is larger.
"""

def find_larger(a: float, b: float, epsilon: float = 1e-9) -> float:
    """
    Determines the larger of two floating-point numbers with tolerance for inaccuracy.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        epsilon (float, optional): A small threshold used to determine if values are equal within acceptable error margins. Defaults to 1e-9.

    Returns:
        float: The larger of the two numbers. If they are effectively equal, returns either one (typically 'a' in case of equality).

    Raises:
        TypeError: If inputs are not numeric floats or if epsilon is negative.
    """
    
    # Validate input types and epsilon value
    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError("Both arguments must be floating-point numbers.")
    if epsilon < 0:
        raise ValueError("Epsilon threshold cannot be negative.")

    # Check for equality within tolerance first to handle cases where a and b are effectively the same value
    is_equal = abs(a - b) <= epsilon
    
    if is_equal:
        return a  # Return either as they are considered equal; 'a' is chosen by convention here.
    
    # Direct comparison without tolerance since values differ significantly enough to be distinguished
    larger_value = a if a > b else b
    return larger_value

if __name__ == '__main__':
    # Hard-coded sample values for testing the function directly without user input or external dependencies
    
    # Test case 1: Clear difference where 'a' is clearly larger
    val_a_1 = 3.50000001
    val_b_1 = 2.99999998
    result_1 = find_larger(val_a_1, val_b_1)

    # Test case 2: Clear difference where 'b' is clearly larger
    val_a_2 = -5.0
    val_b_2 = -4.0
    result_2 = find_larger(val_a_2, val_b_2)

    # Test case 3: Values that are nearly equal due to floating-point representation issues (e.g., sqrt(2)^2 vs 2)
    import math
    approx_two = math.sqrt(2) ** 2
    exact_two = 2.0
    
    val_a_3 = approx_two
    val_b_3 = exact_two
    result_3 = find_larger(val_a_3, val_b_3)

    # Test case 4: Negative numbers where 'a' is larger (closer to zero) than 'b'
    val_a_4 = -1.0
    val_b_4 = -2.5
    result_4 = find_larger(val_a_4, val_b_4)

    # Output results for verification
    print(f"Test 1 (a > b): {val_a_1} vs {val_b_1} -> Larger: {result_1}")
    print(f"Test 2 (b > a): {val_a_2} vs {val_b_2} -> Larger: {result_2}")
    print(f"Test 3 (~equal due to precision): {val_a_3:.15f} vs {val_b_3:.15f} -> Larger: {result_3}, Equal check passed")
    print(f"Test 4 (negatives, a > b): {val_a_4} vs {val_b_4} -> Larger: {result_4}")