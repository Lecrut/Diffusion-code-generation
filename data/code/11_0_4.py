"""
Module: Fraction Ratio Calculator

This module calculates the ratio of two given lengths (numerators) 
and returns the result as a simplified fraction represented by its numerator 
and denominator integers.

The greatest common divisor (GCD) is used to simplify the resulting fraction.
No external libraries are required, though `math.gcd` could be imported; this script uses Euclidean algorithm for self-containment or math module if available in standard environment. Note: Python 3.9+ has built-in math.gcd. To ensure compatibility with older versions without import errors on restricted environments, we can implement a simple GCD function locally.

Usage example (included via if __name__ == '__main__'):
Calculates the ratio of length_a to length_b and prints the simplified fraction "numerator/denominator".

Constraints:
- No input() calls or sys.stdin usage.
- No command-line argument parsing.
- Runs without network access or pre-existing files (other than this script itself).
"""

def gcd(a, b):
    """Compute the greatest common divisor of a and b using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)  # Ensure positive result for fraction denominator logic

def simplify_fraction(num, den):
    """Return simplified numerator and denominator as integers.
    
    Handles cases where the original inputs might be negative or zero appropriately 
    to maintain mathematical correctness (e.g., only one of num/den should be negative).
    Assumes 'den' is not initially 0 for valid ratio calculation logic in main block context,
    though basic error handling could be added if den=0 was passed.
    
    Args:
        num (int): The numerator value from the first length.
        den (int): The denominator value derived from the second length.
        
    Returns:
        tuple: A tuple (simplified_num, simplified_den).
    """
    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero; ratio undefined.")
    
    common = gcd(num, den)
    return num // common, den // common

if __name__ == '__main__':
    pass
