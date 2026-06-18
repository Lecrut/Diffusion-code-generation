"""
Script to calculate the ratio of two lengths as a simplified fraction (numerator/denominator).

This module defines functions to compute the greatest common divisor, simplify fractions,
and perform division resulting in rational numbers without floating-point inaccuracies.
It includes example usage via an `if __name__ == '__main__':` block with hard-coded inputs.
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

def simplify_fraction(numerator: float, denominator: float) -> tuple[int, int]:
    """
    Simplify two numbers into their integer fraction form (numerator/denominator).

    Since the input lengths are expected to be positive floats representing physical quantities,
    we first scale them up by a common factor to convert them into integers. A large multiplier 
    like 10**9 is chosen to maintain precision for typical length values within standard ranges.

    Args:
        numerator (float): The top value of the fraction.
        denominator (float): The bottom value of the fraction.

    Returns:
        tuple[int, int]: A simplified integer ratio (final_numerator, final_denominator).
                       If inputs are equal, returns a single number wrapped in a 1/1 structure 
                       or just that number if they simplify to an integer.
    """
    # Handle edge case where both are zero
    if numerator == denominator and numerator != 0:
        return (numerator // gcd(numerator, denominator), numerator)

    multiplier = 10 ** 9
    
    # Convert floats to integers by scaling up sufficiently to avoid precision loss issues 
    # while keeping the numbers manageable for GCD calculation.
    n_int = int(round((numerator * multiplier)))
    d_int = int(round((denominator * multiplier)))

    common_divisor = gcd(n_int, d_int)

    return (n_int // common_divisor, d_int // common_divisor)

def calculate_ratio(length1: float, length2: float) -> str | tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.

    Args:
        length1 (float): The first length value.
        length2 (float): The second length value.

    Returns:
        Union[str, Tuple[int, int]]: 
            - If the result is an integer, returns just that number or "n/1".
            - Otherwise, returns a tuple of integers representing n/d where d > 1.
              Alternatively formatted as string "n/d" if preferred for display clarity in examples.

    Note: This function ensures no external dependencies like input() or sys.stdin are used.
    """
    # Ensure denominator is not zero to avoid errors, though physical lengths usually aren't zero here.
    if length2 == 0:
        raise ValueError("Denominator cannot be zero.")

    simplified = simplify_fraction(length1, length2)
    
    num, den = simplified
    
    # If the fraction simplifies to an integer (denominator becomes 1), return that or "n/1" string.
    if den == 1:
        result_str = f"{num}"
        return result_str

    return str(f"{num}/{den}")

if __name__ == '__main__':
    # Hard-coded sample values representing lengths of two objects (e.g., meters).
    len_a = 3.5
    len_b = 7.0
    
    ratio_result = calculate_ratio(len_a, len_b)

    print(f"Ratio of {len_a} to {len_b}:")
    
    # Check if the result is a string (non-integer fraction or integer formatted as string logic above simplified it)
    if isinstance(ratio_result, tuple):
        num, den = ratio_result
        print(f"Simplified Fraction: {num}/{den}")
    else:
        print(f"Result ({ratio_result}) represents an exact value.")