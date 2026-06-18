from fractions import Fraction

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).

    The function computes the fraction a/b and returns it in its simplest form.
    
    Args:
        length_a (float): A positive number representing the first length.
        length_b (float): A positive number representing the second length.
        
    Returns:
        tuple[int, int]: A tuple containing two integers that represent the simplified ratio.

    Example:
        >>> calculate_length_ratio(2.0, 4.0)
        (1, 2)
        >>> calculate_length_ratio(3.5, 7.0)
        (1, 2)
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Use Fraction to handle potential floating-point inaccuracies and automatically simplify.
    fraction = Fraction(length_a / length_b).limit_denominator()
    
    return (fraction.numerator, fraction.denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    test_cases = [
        ((2.0, 4.0), (1, 2)),           # Simple even ratio
        ((3.5, 7.0), (1, 2)),          # Decimal conversion to integer ratio
        ((10.0, 10.0), (1, 1)),        # Equal values
        ((5.4, 9.0), (3, 5)),          # Another decimal case (5.4/9 = 0.6 = 3/5)
    ]

    for inputs, expected in test_cases:
        length_a, length_b = inputs
        result = calculate_length_ratio(length_a, length_b)
        
        if result == expected:
            print(f"Input ({length_a}, {length_b}) -> Output: {result} (PASSED)")
        else:
            print(f"Input ({length_a}, {length_b}) -> Expected: {expected}, Got: {result} (FAILED)")

    # Additional verification with a specific case mentioned in the prompt logic implicitly
    result_check = calculate_length_ratio(2, 3)
    assert result_check == (2, 3), "Basic integer input check failed"
    print(f"Straight integers check passed: {result_check}")