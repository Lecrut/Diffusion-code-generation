"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD)
and reduce two integers into their simplest fractional form.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two non-negative integers using Euclid's algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if a == 0 or b == 0:
        return max(a, b)
    
    # Ensure both are positive for the algorithm logic
    x, y = abs(a), abs(b)
    
    while y != 0:
        x, y = y, x % y
    
    return x

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a fraction by dividing both the numerator and denominator 
    by their greatest common divisor.

    Args:
        numerator (int): The top number of the fraction.
        denominator (int): The bottom number of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                          If the result is a whole number, returns (whole_number, 1).
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def calculate_ratio(length_a: int, length_b: int) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    Args:
        length_a (int): The first length value.
        length_b (int): The second length value.

    Returns:
        tuple[int, int]: A tuple (numerator, denominator) representing 
                         the simplified ratio length_a / length_b.
    
    Raises:
        ValueError: If either input is zero or if any other invalid constraints exist.
    """
    # Constraint check based on problem requirements for meaningful ratios usually involving positive lengths
    if not isinstance(length_a, int) or not isinstance(length_b, int):
        raise TypeError("Lengths must be integers.")
    
    if length_a == 0 and length_b != 0:
        return (0, 1) # Zero ratio
    
    simplified_num, simplified_den = simplify_fraction(length_a, length_b)
    
    # Ensure the sign convention is consistent (usually positive denominator)
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
        
    return simplified_num, simplified_den

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Sample inputs representing lengths of two segments.
    length_a_sample = 1200
    length_b_sample = 450
    
    result_numerator, result_denominator = calculate_ratio(length_a_sample, length_b_sample)
    
    print(f"Ratio for {length_a_sample} : {length_b_sample}")
    print(f"Simplified Fraction: {result_numerator}/{result_denominator}")