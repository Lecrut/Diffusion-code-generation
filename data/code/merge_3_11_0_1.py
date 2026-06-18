"""
Script to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD)
and reduce fractions, then provides a main function that calculates and returns
the ratio between two input numbers in its simplest form.
"""

def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two integers using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_fraction(numerator: float, denominator: float) -> tuple[int, int]:
    """
    Simplify a fraction defined by numerator and denominator.

    Args:
        numerator (float): The top value of the fraction.
        denominator (float): The bottom value of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.
    
    Note: Floating point inputs are converted to integers by rounding them first 
    before calculating GCD to avoid precision issues with float arithmetic in this context.
    """
    # Convert floats to nearest integers for integer-based fraction logic
    num = round(numerator)
    den = round(denominator)

    if den == 0:
        raise ValueError("Denominator cannot be zero.")

    common_divisor = gcd(num, den)

    simplified_num = num // common_divisor
    simplified_den = den // common_divisor

    return int(simplified_num), int(simplified_den)

def calculate_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    Args:
        length_a (float): The first length value.
        length_b (float): The second length value.

    Returns:
        tuple[int, int]: A tuple representing the numerator and denominator 
                         of the simplified ratio.
    
    Raises:
        ValueError: If either input is zero or negative where a physical interpretation might be expected,
                   though mathematically valid for any non-zero denominator in this specific calculation logic.
    """
    if length_b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    # Perform division to get the ratio value as a float first
    ratio_value = length_a / length_b
    
    return simplify_fraction(ratio_value, 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    SAMPLE_LENGTH_A = 850.0
    SAMPLE_LENGTH_B = 250.0

    numerator, denominator = calculate_ratio(SAMPLE_LENGTH_A, SAMPLE_LENGTH_B)
    
    print(f"Ratio of {SAMPLE_LENGTH_A} to {SAMPLE_LENGTH_B}:")
    print(f"Simplified Fraction: {numerator}/{denominator}")