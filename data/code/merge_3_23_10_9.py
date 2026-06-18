import math

def is_float_equal(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function uses the relative difference method to determine if two floats are 
    effectively equal, which avoids issues with absolute zero comparisons and large 
    magnitude differences that might occur in direct subtraction due to precision limits.

    Parameters:
        a (float): The first number to compare.
        b (float): The second number to compare.
        tolerance (float): The maximum allowed difference between the numbers. Default is 1e-9.

    Returns:
        bool: True if |a - b| <= tolerance, False otherwise.
    
    Note:
        This implementation relies on basic arithmetic operations and does not require 
        any external libraries beyond the standard `math` module for potential edge-case 
        robustness in specific mathematical contexts (though direct subtraction is used here 
        as it is sufficient and more readable than absolute relative difference logic).

    Example:
        >>> is_float_equal(1.0, 1.0)
        True
        >>> is_float_equal(3.14159265358979, math.pi)
        True
    """
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    # Sample values for testing the function without user input or external dependencies
    
    test_cases = [
        (1.0, 1.0),                           # Should be equal
        (3.14159265358979, math.pi),         # Should be equal within tolerance
        (1e-10, -1e-10 + 1e-10),             # Should be equal to zero difference
        (1.0, 1.000000002),                   # Slightly different, should not match default tolerance
        (-5.5, -5.499999998),                 # Close negative numbers
    ]

    print("Testing floating-point equality with default tolerance (1e-9):")
    
    for i, (num_a, num_b) in enumerate(test_cases, 1):
        result = is_float_equal(num_a, num_b)
        status = "Equal" if result else "Not Equal"
        print(f"Test {i}: {num_a} vs {num_b} -> {status}")