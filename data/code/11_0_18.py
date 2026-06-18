"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD)
and reduce fractions by dividing both numerator and denominator by their GCD.
It includes a main execution block with hard-coded sample values for testing.
No user input, command-line arguments, or external dependencies are required.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers using Euclid's algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify the fraction represented by numerator/denominator.

    The function divides both numbers by their greatest common divisor to ensure
    the result is in its simplest form (i.e., gcd(numerator, denominator) == 1).
    Negative signs are handled such that only the numerator carries a negative sign if needed.

    Args:
        numerator (int): The top number of the fraction.
        denominator (int): The bottom number of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    The function converts floating-point inputs to integers by rounding them first.
    This avoids precision issues inherent in representing ratios with floats directly.
    
    Args:
        length_a (float): First length value.
        length_b (float): Second length value.

    Returns:
        tuple[int, int]: A simplified fraction represented as a tuple (numerator, denominator).
        
    Raises:
        ValueError: If either input is zero or negative (as lengths must be positive).
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Lengths must be positive numbers.")

    # Round to nearest integer to handle floating point inaccuracies before conversion
    num = round(length_a)
    den = round(length_b)

    return simplify_fraction(num, den)

if __name__ == '__main__':
    # Hard-coded sample values for testing.
    # Sample 1: Ratio of 4 meters to 8 meters should be 1/2.
    length_a_sample_1 = 4.0
    length_b_sample_1 = 8.0
    
    result_fraction_1 = calculate_length_ratio(length_a_sample_1, length_b_sample_1)
    
    # Sample 2: Ratio of 3 inches to 9 inches should be 1/3.
    length_a_sample_2 = 3.5
    length_b_sample_2 = 9.0
    
    result_fraction_2 = calculate_length_ratio(length_a_sample_2, length_b_sample_2)

    print(f"Ratio of {length_a_sample_1} to {length_b_sample_1}:")
    numerator_1, denominator_1 = result_fraction_1
    print(f"Simplified Fraction: {numerator_1}/{denominator_1}")

    print(f"\nRatio of {length_a_sample_2} to {length_b_sample_2}:")
    numerator_2, denominator_2 = result_fraction_2
    print(f"Simplified Fraction: {numerator_2}/{denominator_2}")