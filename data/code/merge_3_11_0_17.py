"""
Module to calculate the ratio of two lengths as a simplified fraction.

This script defines a function that takes two positive numbers representing 
lengths, calculates their quotient in fractional form (numerator/denominator),
and returns these values reduced by their greatest common divisor (GCD).
The result ensures no floating-point approximation is used; instead, the exact
rational representation is maintained.

No user input or command-line arguments are required for operation.
"""

def calculate_length_ratio(length1: float, length2: float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths as a simplified fraction (numerator/denominator).

    Args:
        length1 (float): The first positive length value.
        length2 (float): The second positive length value.

    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator 
                         of the simplified ratio. Both values are integers >= 0.

    Raises:
        ValueError: If either input is not a number or if it is zero/divide-by-zero logic applies (denominator cannot be zero in standard math but here we handle division carefully). 

        Note: While strictly speaking, dividing by zero causes an exception, 
              this function expects length2 > 0. In real-world lengths, 
              negative values would imply directionality not suitable for simple ratio magnitude usually requested without context of vectors. Assuming positive magnitudes here per typical usage in such problems unless otherwise specified as signed integers or floats where signs matter (then numerator carries sign).

        Since task requires handling "lengths", we assume non-negative inputs; 
              if length2 is 0, behavior follows mathematical division rule which raises ZeroDivisionError naturally to be safe and correct.
    """
    
    # Validate input types
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise TypeError("Inputs must be numbers.")

    length1 = int(length1)
    length2 = int(length2)  # Convert to integers for exact fraction arithmetic
    
    if length2 == 0:
        raise ZeroDivisionError(f"Second length cannot be zero. Input was {length2}.")
        
    numerator = length1
    denominator = length2

    common_divisor = _gcd(numerator, denominator)
    
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor
    
    return (simplified_num, simplified_den)

def _gcd(a: int, b: int) -> int:
    """
    Helper function to compute the Greatest Common Divisor using Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b.
    """
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD inputs must be integers.")
        
    while b:
        temp = b
        b = a % b
        a = temp
    
    return max(0, a)

if __name__ == '__main__':
    # Sample values run without user input or external dependencies.
    
    sample_lengths_1 = 64
    sample_lengths_2 = 32

    numerator_result, denominator_result = calculate_length_ratio(sample_lengths_1, sample_lengths_2)

    print(f"Ratio of {sample_lengths_1} to {sample_lengths_2}: {numerator_result}/{denominator_result}")