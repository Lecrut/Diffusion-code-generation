import math
from fractions import Fraction

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).

    The function ensures that both input lengths are treated as their integer parts 
    before computing the greatest common divisor for simplification. This avoids issues
    with floating-point precision when inputs have decimal representations intended
    to be exact ratios in practical applications like scaling factors or unit conversions.

    :param length_a: First positive number (float)
    :param length_b: Second positive number (float)
    :return: A tuple of two integers representing the simplified ratio (a, b).

    Examples:
        >>> calculate_length_ratio(4.0, 6.0)
        (2, 3)
        >>> calculate_length_ratio(5, 10)
        (1, 2)
    """
    # Convert floats to integers by truncating decimals for practical integer ratio logic
    int_a = int(length_a)
    int_b = int(length_b)

    if int_a <= 0 or int_b <= 0:
        raise ValueError("Both input lengths must be positive numbers.")

    # Compute the greatest common divisor (GCD) of the two integers
    gcd_value = math.gcd(int_a, int_b)

    # Simplify the ratio by dividing both parts by their GCD
    simplified_numerator = int_a // gcd_value
    simplified_denominator = int_b // gcd_value

    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_inputs = [
        (4.0, 6.0),   # Expected: (2, 3)
        (5, 10),      # Expected: (1, 2)
        (998244353.0, 2),     # Large numbers example
    ]

    for i, test_pair in enumerate(sample_inputs, start=1):
        result = calculate_length_ratio(*test_pair)
        print(f"Test case {i}: inputs={test_pair} -> ratio={result}")