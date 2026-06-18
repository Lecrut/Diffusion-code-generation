"""
Script to compare two floating-point numbers with epsilon handling.

This module defines a function that compares two floats, accounting for 
floating-point representation inaccuracies by using a small tolerance value (epsilon).
It determines which number is larger or if they are effectively equal within the tolerance.
"""

def compare_floats(a: float, b: float) -> str:
    """
    Compare two floating-point numbers with epsilon handling.

    Args:
        a (float): The first numeric value to compare.
        b (float): The second numeric value to compare.

    Returns:
        str: A string indicating the relationship between 'a' and 'b'.
             - "A is larger" if a > b + epsilon
             - "B is larger" if b > a + epsilon
             - "Numbers are equal (within tolerance)" otherwise
    """
    # Define an appropriate epsilon for float comparison. 
    # 1e-9 is commonly used as it balances precision and performance needs.
    EPSILON = 1e-9

    diff = abs(a - b)

    if diff > EPSILON:
        if a > b + EPSILON:
            return "A is larger"
        else:
            return "B is larger"
    
    # If the difference is within epsilon, they are considered equal.
    return "Numbers are equal (within tolerance)"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    val_a = 3.141592653589793
    val_b = 3.141592653589793
    
    result_equal = compare_floats(val_a, val_b)

    # Sample case where values are slightly different due to floating-point arithmetic simulation
    val_c = 0.1 + 0.2
    val_d = 0.3
    
    result_diff_simulated = compare_floats(val_c, val_d)

    print(f"Comparison of {val_a} and {val_b}:")
    print(result_equal)
    
    print("\nComparison of simulated float addition (0.1 + 0.2) vs 0.3:")
    print(f"{val_c} = {format(val_c, '.17f')}")
    print(f"{val_d} = {format(val_d, '.17f')}")
    print(result_diff_simulated)

    # Additional explicit test case where one is clearly larger
    val_e = 5.0
    val_f = 4.9
    
    result_clear = compare_floats(val_e, val_f)
    print(f"\nComparison of {val_e} and {val_f}:")
    print(result_clear)