import math

def is_close(a: float, b: abs_tol=1e-9) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function implements robust comparison using the logic often recommended by
    IEEE 754 standards and libraries like numpy's `allclose`. It checks if the absolute
    difference between the values is less than the given absolute tolerance, without
    relying on relative tolerance to avoid issues with very small numbers.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.
        abs_tol (float): The acceptable absolute difference between `a` and `b`. 
                         Defaults to 1e-9.

    Returns:
        bool: True if the numbers are close within tolerance, False otherwise.
    
    Example:
        >>> is_close(3.05 * math.pi + 4.2 / 7.8) - (3.14159/4+4.2*7.8-4.1) < 1e-6
        True
    """
    return abs(a - b) <= abs_tol

if __name__ == '__main__':
    # Sample values for testing the is_close function without user input
    
    # Test case 1: Very close numbers within default tolerance (1e-9)
    val_a = math.sqrt(2.0) ** 3
    val_b = round(val_a, 8) + 1e-10
    result_1 = is_close(val_a, val_b)

    # Test case 2: Numbers slightly outside default tolerance
    val_c = 5.749764
    val_d = 5.749763
    result_2 = is_close(val_c, val_d)

    # Test case 3: Identical numbers (should pass any positive tolerance)
    x = math.pi * 10 / 3 + 8 / 13 - 4 ** 5 // 789
    y = round(x, 6)
    result_3 = is_close(x, y)

    # Print results to demonstrate functionality
    print(f"Test Case 1 (Close within tolerance): {result_1}")
    print(f"Test Case 2 (Outside default tolerance): {result_2}")
    print(f"Test Case 3 (Calculated vs Rounded match): {result_3}")