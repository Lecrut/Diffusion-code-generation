import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a', b').
    
    The function converts the floating-point inputs to fractions by finding their 
    greatest common divisor after scaling them appropriately. It returns the reduced 
    integer representation of the ratio.

    Args:
        length_a (float): A positive number representing the first dimension/length.
        length_b (float): A positive number representing the second dimension/length.

    Returns:
        tuple[int, int]: A tuple containing two integers that represent the simplified 
                         ratio of length_a to length_b.

    Raises:
        ValueError: If either input is not a positive number.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both inputs must be positive numbers.")

    # Convert floats to integers by multiplying with the least common multiple of their denominators 
    # derived from rounding errors, effectively treating them as exact rationals for simplification.
    # We use a large multiplier (1e9) scaled down if necessary or just round after scaling up significantly
    # to avoid precision issues inherent in float representation. A robust approach is:
    # 1. Multiply both by a sufficiently large power of 10 based on decimal places, 
    # but since we don't know exact decimals, we can use the math.gcd logic directly on scaled integers.
    
    # To handle floating point inaccuracies (e.g., 2/3 represented as float), we scale them up to integers first.
    # We choose a scaling factor that covers typical precision needs or rely on gcd of rounded values if they are close enough.
    # However, the most robust way without knowing exact decimal places is to:
    # - Scale both numbers by 10^N where N is max(ceil(log10(max(a,b)*precision))) 
    # But simpler for general cases: convert to a common scale or use fractions module logic manually.
    
    # Let's assume the inputs are meant to be treated as exact values within reasonable float precision limits.
    # We will multiply both by 1,000,000 (or enough to capture typical input scales) and round to integers.
    # If higher precision is needed dynamically:
    
    scale_factor = 1_000_000
    
    int_a = round(length_a * scale_factor)
    int_b = round(length_b * scale_factor)

    if int_a == 0 or int_b == 0:
        raise ValueError("Inputs are not positive.")

    common_divisor = math.gcd(int_a, int_b)
    
    return (int_a // common_divisor, int_b // common_divisor)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (10.5, 21.0),      # Expected: (1, 2)
        (3.0, 4.5),       # Expected: (2, 3) -> scaled and reduced
        (7/3, 14/9),      # Float representation of fractions
        (1.0, 1.0),       # Expected: (1, 1)
    ]

    for a, b in samples:
        result = calculate_length_ratio(a, b)
        print(f"Ratio of {a} and {b}: {result}")