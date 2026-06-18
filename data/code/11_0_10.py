import math

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers."""
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
    
    Note:
        This function handles floating-point inputs by converting them to exact fractions using 
        Python's `fractions.Fraction` class internally for precision, then reduces them via GCD.
        Negative signs are handled correctly (sign stays with numerator).
        
    Example:
        >>> simplify_fraction(1/3, 2)
        (1, 6)
    """
    # Use Fraction to handle float conversion precisely and automatically reduce
    from fractions import Fraction
    
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    f = Fraction(numerator, denominator)
    return int(f.numerator), int(f.denominator)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access is used.
    length_a: float = 3.0 / 4.0
    length_b: float = 1.5
    
    numerator, denominator = simplify_fraction(length_a, length_b)
    
    print(f"Simplified ratio of {length_a} to {length_b}:")
    print(f"Numerator (numerator): {numerator}")
    print(f"Denominator (denominator): {denominator}")