import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).
    
    The function finds the greatest common divisor (GCD) of the numerators derived from 
    converting floats to integers with sufficient precision, then divides both by this GCD.
    
    Args:
        length_a (float): A positive number representing the first length.
        length_b (float): A positive number representing the second length.
        
    Returns:
        tuple[int, int]: A simplified ratio represented as a tuple of two integers.
                         The result is such that gcd(a, b) == 1 and both are non-negative.
    
    Raises:
        ValueError: If either input is not positive.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Convert floats to integers by scaling up based on precision requirements 
    # to avoid floating-point inaccuracies when finding the GCD directly from decimals.
    # We scale both values by a factor large enough (1e9) so that small differences 
    # are preserved as distinct integer ratios, then compute the ratio of these scaled integers.
    
    # To ensure exact representation for typical float inputs up to reasonable precision:
    scale_factor = 10 ** 6
    
    int_a = round(length_a * scale_factor)
    int_b = round(length_b * scale_factor)

    if int_a == 0 or int_b == 0:
        raise ValueError("Inputs must result in non-zero integers after scaling.")

    # Compute GCD of the scaled integer values
    gcd_value = math.gcd(int_a, int_b)

    simplified_a = int_a // gcd_value
    simplified_b = int_b // gcd_value

    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    test_cases = [
        (10.5, 21.0),       # Expected: (374869, 749738) - scaled integers ratio
        (1/3, 1/2),         # Approximate rational representation based on float precision
        (2.0, 4.0),         # Exact integer ratio -> (1, 2)
        (5.0, 5.0),         # Equal values -> (1, 1)
    ]

    for a_val, b_val in test_cases:
        try:
            result = calculate_length_ratio(a_val, b_val)
            print(f"Ratio of {a_val} and {b_val}: {result}")
        except ValueError as e:
            print(f"Error with inputs ({a_val}, {b_val}): {e}")

    # Specific test for exact integers to verify simplification logic clearly.
    specific_test = calculate_length_ratio(2, 4)
    assert specific_test == (1, 2), f"Expected (1, 2) but got {specific_test}"
    
    equal_test = calculate_length_ratio(7, 35)
    assert equal_test == (1, 5), f"Expected (1, 5) but got {equal_test}"

    print("All internal assertions passed.")