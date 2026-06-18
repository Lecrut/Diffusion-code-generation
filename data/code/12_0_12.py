import math

def get_gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers."""
    return math.gcd(int(a), int(b))

def simplify_ratio(ratio_tuple):
    """
    Simplify a weight ratio tuple to its lowest terms.

    Args:
        ratio_tuple (tuple or list): Two numeric values representing weights.

    Returns:
        tuple: A simplified tuple of integers in the format (numerator, denominator).
    """
    # Convert input to float for division handling, then back to int if needed later
    a = float(ratio_tuple[0])
    b = float(ratio_tuple[1])

    # Handle zero case explicitly to avoid ZeroDivisionError during logic flow, 
    # though math.gcd handles 0 gracefully in most cases.
    common_divisor = get_gcd(a, b)

    simplified_numerator = a / common_divisor if common_divisor != 0 else int(b)
    simplified_denominator = b / common_divisor if common_divisor != 0 else int(simplified_numerator)

    # Ensure the result is returned as integers (assuming inputs are proportional to integers)
    return tuple(int(x) for x in [simplified_numerator, simplified_denominator])

if __name__ == '__main__':
    sample_ratios = [(150, 250), (3.6, 7.2)]

    print("Sample Input Ratios:")
    for ratio in sample_ratios:
        result = simplify_ratio(ratio)
        print(f"Ratio {ratio} simplified to {result}")