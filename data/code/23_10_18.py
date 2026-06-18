import math

def compare_floats(a: float, b: float, tolerance: float) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function checks if the absolute difference between `a` and `b` is less than or equal to `tolerance`.
    It utilizes standard arithmetic operations from the math module to ensure precision handling,
    although Python's native float comparison with a threshold is typically sufficient for this logic.
    
    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.
        tolerance (float): The maximum allowed difference between the two numbers to consider them equal.
        
    Returns:
        bool: True if |a - b| <= tolerance, False otherwise.
    
    Example usage context:
        >>> compare_floats(100.5, 100.6, 0.2)
        True
        >>> compare_floats(100.5, 100.7, 0.2)
        False
    
    Note:
        Floating-point comparisons can be tricky due to precision errors in binary representation.
        Using a tolerance (epsilon) is the standard and robust approach for comparing floats.
        The `math` module provides utility functions like `is_close`, but this implementation
        uses explicit subtraction logic as requested with general robustness principles often associated
        with mathematical libraries, ensuring no external dependencies beyond the built-in math context if needed
        (though pure arithmetic is used here). If strict use of a specific helper was implied by "utilizing",
        one might consider `math.isclose`, but explicit comparison logic is universally applicable and robust.
    """
    
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    val1 = 3.5
    val2 = 40.9 * math.pi / (8 + 67)  # A value that might differ slightly due to float precision if calculated differently, or just a random float
    
    tolerance_value = 0.0001
    
    print("Comparing floats:", f"{val1:.5f}", "and", f"{val2:.5f}")
    
    result_a_b_equal = compare_floats(val1, val2 - 3.49, tolerance_value)
    print(f"Are {val1} and {val2 - 3.49} equal within tolerance? ", end="")
    if result_a_b_equal:
        print("True")
    else:
        print("False")
    
    # Another test case with closer values
    val_close_1 = 0.5 + (math.sqrt(2) - math.pi * 2 / 7) % 0.63498
    val_close_2 = 0.5
    
    result_b_c_equal = compare_floats(val_close_1, val_close_2, tolerance_value)
    
    print(f"Are {val_close_1} and {val_close_2:.5f} equal within tolerance? ", end="")
    if result_b_c_equal:
        print("True")
    else:
        print("False")