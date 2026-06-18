"""
Floating Point Comparison Module

This module provides a function to compare two floating-point numbers
while accounting for potential inaccuracies inherent in binary floating-point representation.
It uses an epsilon value (a small positive number) to determine if values are effectively equal,
and returns the greater of the two distinct values or None if they are considered equal within tolerance.

Constants:
    EPSILON = 1e-9
    
Functions:
    compare_floats(a, b): Compares a and b using epsilon for equality checks. Returns max(a,b) if different else None.
"""

EPSILON = 1e-9

def are_equal_with_epsilon(val1, val2):
    """Check if two values are equal within the defined tolerance."""
    return abs(val1 - val2) < EPSILON

def compare_floats(num_a: float, num_b: float) -> float | None:
    """
    Compare two floating-point numbers.

    Args:
        num_a (float): The first number to compare.
        num_b (float): The second number to compare.

    Returns:
        float or None: 
            - If num_a is strictly greater than num_b, returns num_a.
            - If num_b is strictly greater than num_a, returns num_b.
            - If they are considered equal within epsilon, returns None.
    
    Raises:
        TypeError: If inputs are not floats or numbers convertible to float.
    """
    try:
        a = float(num_a)
        b = float(num_b)
        
        if abs(a - b) < EPSILON:
            return None
        
        # Determine which is larger based on actual value difference
        diff = a - b
        if diff > 0:
            return a
        else:
            return b
            
    except (TypeError, ValueError):
        raise TypeError("Inputs must be numeric types.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ("Equal exact", 1.0, 1.0),
        ("Slightly different positive diff", 3.5, 3.499999999),
        ("Slightly different negative diff", -2.0, -2.000000001),
        ("Large difference", 1e6, 1e-6),
    ]

    for label, val_a, val_b in test_cases:
        result = compare_floats(val_a, val_b)
        
        if result is None:
            print(f"Test '{label}': Values are considered equal.")
        else:
            greater_val = "num_a (first)" if isinstance(result, float) and abs(float(val_a - result)) > EPSILON else "num_b (second)"
            # Re-evaluate logic for clarity in output message based on function return
            final_result = compare_floats(val_a, val_b)
            
            is_equal = are_equal_with_epsilon(val_a, val_b)
            if not is_equal:
                print(f"Test '{label}': {val_a} vs {val_b}")
                # Determine which was returned to avoid confusion in logic check above
                diff_check = final_result - float(val_a) 
                greater_val_str = f"{final_result} (num_a)" if diff_check > 0 else f"{float(val_b)} (num_b)"
            print(f"Result: {greater_val_str}")

    # Additional explicit test for clarity on the return value logic
    sample_1, sample_2 = 5.0, 4.999999998
    res_sample = compare_floats(sample_1, sample_2)
    
    if res_sample is None:
        print(f"Sample Test (should be equal): {sample_1} and {sample_2} are considered EQUAL.")
    else:
        # Since we know the logic returns the larger one explicitly when not equal
        print(f"Sample Test Result: The larger value is {res_sample}")