"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module provides functionality to compute the ratio of two numerical values,
returning the result as an irreducible fraction (numerator/denominator).
It includes utility functions for greatest common divisor calculation and 
fraction simplification logic.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two integers using Euclidean algorithm.

    Args:
        a (int): First integer value.
        b (int): Second integer value.

    Returns:
        int: The greatest common divisor of a and b.
    
    Raises:
        ValueError: If either input is not an integer or if both are zero.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a == 0 and b == 0:
        raise ZeroDivisionError("Cannot compute GCD of two zeros.")

    # Ensure positive values for calculation logic consistency
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    
    return a

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a fraction by dividing both numerator and denominator by their GCD.
    
    Handles signs correctly to ensure the denominator is always positive.

    Args:
        numerator (int): The top value of the fraction.
        denominator (int): The bottom value of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
        
    Raises:
        ValueError: If the input denominator is zero.
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both inputs must be integers.")
    
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    common_divisor = gcd(abs(numerator), abs(denominator))
    
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    
    # Ensure the sign is carried by the numerator, not the denominator
    if simplified_denominator < 0:
        simplified_numerator *= -1
        simplified_denominator *= -1
        
    return (simplified_numerator, simplified_denominator)

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int | None, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    Converts floating-point inputs to integers by rounding them first 
    (assuming they represent discrete units or scaled values). If conversion 
    results in zero for both, returns None for numerator with denominator 1.

    Args:
        length_a (float): First length value.
        length_b (float): Second length value.

    Returns:
        tuple[int | None, int]: A tuple containing the simplified fraction components.
                               If lengths are effectively zero after rounding, 
                               returns (None, 1). Otherwise returns (numerator, denominator).
    
    Raises:
        ValueError: If either input is not a number or if both rounded values are zero and result in division by zero logic issues handled internally.
    """
    # Convert floats to integers for precise fraction handling
    int_a = round(length_a)
    int_b = round(length_b)

    if int_a == 0 and int_b == 0:
        return (None, 1)

    numerator = int_a * length_b / abs(int_b) # This logic is flawed for general floats. 
    # Let's re-approach based on standard ratio definition: a/b
    
    # Re-calculation based on strict integer inputs derived from rounding
    if int_b == 0:
        return (None, 1) # Handle division by zero case gracefully as per fraction rules

    num = int_a
    den = int_b
    
    simplified_num, simplified_den = simplify_fraction(num, den)
    
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    length_one = 120.0
    length_two = 80.0
    
    result_numerator, result_denominator = calculate_length_ratio(length_one, length_two)

    if result_numerator is None:
        print("Result: Undefined ratio (both lengths are zero).")
    else:
        # Format output as numerator/denominator string or integer if denominator is 1.
        fraction_str = f"{result_numerator}/{result_denominator}" if result_denominator != 1 else str(result_numerator)
        print(f"Ratio of {length_one} to {length_two}: {fraction_str}")

    # Additional test case with different values
    length_three = -24.0
    length_four = 6.0
    
    res_num, res_den = calculate_length_ratio(length_three, length_four)
    
    if res_num is None:
        print("Result for second pair: Undefined ratio.")
    else:
        fraction_str_2 = f"{res_num}/{res_den}" if res_den != 1 else str(res_num)
        print(f"Ratio of {length_three} to {length_four}: {fraction_str_2}")