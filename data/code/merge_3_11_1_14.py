import math
from fractions import Fraction

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculate the simplified ratio of two positive numbers as a tuple (a/b).
    
    Args:
        length_a: First positive number.
        length_b: Second positive number.
        
    Returns:
        A tuple containing two integers representing the simplified ratio.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Use Fraction to handle floating-point precision issues and automatically simplify
    fraction_result = Fraction(length_a, length_b)
    
    numerator = int(fraction_result.numerator)
    denominator = int(fraction_result.denominator)
    
    return (numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        10.5, 3.5,      # Should simplify to 3/1
        24, 8,           # Should simplify to 3/1
        7, 14,          # Should simplify to 1/2
        16, 24,         # Should simplify to 2/3
    ]

    for i in range(0, len(samples), 2):
        length_a = samples[i]
        length_b = samples[i + 1] if i + 1 < len(samples) else samples[0] * 5
        
        a_simplified_int, b_simplified_int = calculate_length_ratio(length_a, length_b)
        
        print(f"Ratio of {length_a} and {length_b}: ({a_simplified_int}, {b_simplified_int})")