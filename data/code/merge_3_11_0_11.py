"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD)
and then calculates the ratio of two numbers, reducing it to its simplest form.
The result is returned as a tuple containing the numerator and denominator.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two integers using Euclid's algorithm.

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

    Args:
        numerator (int): The top number of the fraction.
        denominator (int): The bottom number of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    
    Note:
        If the input values are zero or negative in a way that doesn't make sense for length ratios,
        this function handles them by returning 0/1 if both inputs are effectively zero 
        (though lengths should be positive), otherwise it preserves signs appropriately.
        For standard length ratios, we assume non-zero denominators after simplification logic.
    """
    # Handle edge case where denominator is zero to avoid division errors later or invalid states
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    common = gcd(numerator, denominator)

    simplified_numerator = numerator // common
    simplified_denominator = denominator // common

    return (simplified_numerator, simplified_denominator)

def calculate_length_ratio(length_a: int | float, length_b: int | float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    Args:
        length_a (int | float): The first length value.
        length_b (int | float): The second length value.

    Returns:
        tuple[int, int]: A tuple representing the numerator and denominator 
                         of the simplified ratio. Both will be integers.
    
    Note:
        Floating point inputs are converted to fractions using Python's Fraction class logic internally 
        by multiplying both sides by a common power of 10 based on decimal places to ensure integer arithmetic,
        then simplifying via GCD. This avoids floating-point precision errors in the final result representation.
    """
    from math import gcd as math_gcd

    # Convert floats to integers scaled appropriately if they are not already whole numbers
    def float_to_scaled_int(value: int | float) -> tuple[int, int]:
        if isinstance(value, (int, float)):
            # Determine the number of decimal places needed for precision up to 10^-9 just in case
            scale = max(10**len(str(float(value)).split('.')[1]) if '.' in str(value) else 1, 
                        10 ** int(-str(abs(min(len(format(value), '.2f').lstrip('-')), -float('inf')))) ) # Simplified logic for demo: assume standard float precision
            # A robust way without complex string parsing for this specific constraint is to use a fixed high scale or Fraction. 
            # Let's stick to the requirement of returning integers in output, so we convert floats to exact representations if possible within reason.
            # To ensure integer inputs for GCD: multiply by 10^N where N covers decimal places.
            
            s_val = str(value)
            if '.' not in s_val:
                return int(value), value * (int(math_gcd(9, 9))) 
                
            parts = s_val.split('.')
            decimals = len(parts[1])
            scale_factor = 10 ** max(decimals, -len(str(abs(float('-inf')))) if False else decimals) # Just use decimal places found
            
            scaled_int = int(round(value * (10 ** decimals)))
            return scaled_int, value
        
        raise TypeError("Inputs must be numeric.")

    num_scaled, den_scaled = float_to_scaled_int(length_a), float_to_scaled_int(length_b)
    
    # Now we have two large integers representing the ratio exactly
    common_divisor = gcd(num_scaled, den_scaled)
    
    final_num = num_scaled // common_divisor
    final_den = den_scaled // common_divisor
    
    return (final_num, final_den)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    length_one = 120
    length_two = 45

    result_numerator, result_denominator = calculate_length_ratio(length_one, length_two)

    print(f"Ratio of {length_one} to {length_two}:")
    print(f"Simplified Fraction: {result_numerator}/{result_denominator}")