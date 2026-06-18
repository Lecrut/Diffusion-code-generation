"""
Module to calculate the ratio of two lengths as a simplified fraction.

This module defines functions to compute the greatest common divisor (GCD)
and then calculates the ratio of two numbers, reducing it to its simplest form.
The result is returned as a tuple containing the numerator and denominator.
No user input or external dependencies are required for execution.
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
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_fraction(numerator: float, denominator: float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths as a simplified fraction.

    This function takes two floating-point numbers representing lengths, converts them to integers (assuming they are whole number ratios),
    finds their GCD, and returns the numerator and denominator divided by this GCD.
    
    Note: If exact integer conversion is not possible due to float precision issues for non-integer inputs that should be treated as fractions,
    a tolerance-based approach or rounding might be needed in real-world scenarios involving measurements. 
    For strict mathematical fraction reduction of integers provided via input (as per the constraint against interactive prompts),
    we assume integer arithmetic is expected after conversion from float if necessary for demonstration purposes with sample values like 10 and 25.

    However, to strictly adhere to "simplified fraction" logic often implying exact rational numbers:
    If inputs are floats that represent integers (e.g., 3.0), we convert them first. 
    Otherwise, this function assumes the caller provides integer-like values or handles float precision by rounding if they are effectively integers.

    For robustness in a general script context without external libraries for arbitrary precision rationals:
    We will assume the sample inputs provided below are intended to be treated as exact numbers (integers). 
    If floats like 10/25 are passed, we convert them to int(3) and int(4) if they represent whole numbers.

    Args:
        numerator (float): The first length value.
        denominator (float): The second length value.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.
    
    Raises:
        ValueError: If either input is zero or if conversion to integer fails due to non-integer float values not matching expected precision.
    """
    # Handle potential floating point inaccuracies by rounding to nearest whole number 
    # assuming inputs are meant to be exact integers (common in such tasks unless specified otherwise).
    try:
        n_int = int(round(numerator))
        d_int = int(round(denominator))
        
        if n_int == 0 or d_int == 0:
            raise ValueError("Numerator and denominator cannot be zero.")

        common_divisor = gcd(n_int, d_int)
        simplified_numerator = n_int // common_divisor
        simplified_denominator = d_int // common_divisor
        
        return (simplified_numerator, simplified_denominator)
    except Exception:
        # Fallback for cases where rounding isn't sufficient or inputs are truly non-integers 
        # but the task implies a specific mathematical reduction. 
        # Given the constraints and typical usage of such scripts with sample values like 10/25,
        # we prioritize integer conversion via rounding as it's standard for "length ratio" problems unless decimals are explicitly required in output format (which contradicts 'simplified fraction' usually implying integers).
        raise ValueError("Inputs must be convertible to exact integers.")

if __name__ == '__main__':
    # Hard-coded sample values representing two lengths.
    length_a = 10
    length_b = 25

    result_numerator, result_denominator = simplify_fraction(length_a, length_b)

    print(f"The ratio of {length_a} to {length_b} is:")
    print(f"{result_numerator}/{result_denominator}")