"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD),
and subsequently simplify fractions represented by numerators and denominators.
It includes an interactive demonstration block using hard-coded values, 
strictly avoiding any user input mechanisms like sys.stdin or argparse arguments.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b.
    """
    # Ensure inputs are treated as positive for the division logic, 
    # though mathematically GCD is defined for non-negative integers typically in this context.
    if a == 0 or b == 0:
        return max(a, b)

    while b != 0:
        a, b = b, a % b
    
    return abs(a)

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify the fraction represented by numerator and denominator.

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

    return numerator // common_divisor, denominator // common_divisor

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int | None, int]:
    """
    Calculate the ratio of two lengths and simplify it into a fraction.

    Floats are converted to integers scaled by 10^6 (or handled via math 
    if precision allows integer conversion for demonstration purposes). 
    For this specific task context without external libraries requiring float handling,
    we assume inputs can be treated as exact values or scale them appropriately.
    
    To ensure a clean implementation returning only ints where possible:
    If the input floats result in non-integers after scaling, they are cast to int
    for demonstration stability (e.g., treating 1/3 as integers scaled). 
    However, strictly following 'ratio of lengths' often implies rational numbers.
    
    Implementation approach: Scale both inputs by a factor of 10^6 and convert to integer.
    This avoids floating point precision issues in the GCD calculation while maintaining accuracy for typical small decimals.

    Args:
        length_a (float): First length value.
        length_b (float): Second length value.

    Returns:
        tuple[int, int]: The simplified numerator and denominator of the ratio a/b.
    
    Note: 
      If b is zero, it returns None for numerator to indicate invalid division logic in this context.
"""
    # Scale inputs to avoid float precision issues during integer GCD calculation
    SCALE_FACTOR = 10_000_000
    
    scaled_a = int(round(length_a * SCALE_FACTOR))
    scaled_b = int(round(length_b * SCALE_FACTOR))

    if scaled_b == 0:
        return None, 0
        
    # The ratio is (scaled_a / scaled_b)
    num = scaled_a
    den = scaled_b
    
    simplified_num, simplified_den = simplify_fraction(num, den)
    
    return simplified_num, simplified_den

if __name__ == '__main__':
    # Hard-coded sample values representing two lengths: 3 units and 4 units.
    length_one = 3.0
    length_two = 4.0
    
    result_ratio_numerator, ratio_result_denominator = calculate_length_ratio(length_one, length_two)

    print(f"The ratio of {length_one} to {length_two} is:")
    if result_ratio_numerator is not None:
        # Using f-string for formatting the fraction clearly as num/den 
        print(f"{result_ratio_numerator}/{ratio_result_denominator}")
    else:
        print("Invalid input (division by zero equivalent).")