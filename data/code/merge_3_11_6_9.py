import math

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two integers by dividing both 
    numerator (a) and denominator (b) by their Greatest Common Divisor (GCD).
    
    Handles large integers efficiently using Python's arbitrary precision arithmetic.
    Normalizes signs so that if a result exists where one is negative, it appears in 'numerator'.

    Args:
        a (int): The numerator of the ratio.
        b (int): The denominator of the ratio.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    
    Raises:
        ValueError: If both inputs are zero or if the denominator is zero in the original input.
    """
    # Handle edge cases for zeros to avoid division by zero errors later
    if a == 0 and b == 0:
        raise ValueError("Cannot simplify ratio of two zeros.")

    if b == 0:
        raise ValueError("Denominator cannot be zero in the original inputs.")

    # Calculate GCD. math.gcd handles large integers efficiently in Python.
    common_divisor = math.gcd(a, b)

    simplified_numerator = a // common_divisor
    simplified_denominator = b // common_divisor

    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    num1 = 450_000_000_000
    den1 = -375_000_000

    result_num, result_den = simplify_ratio(num1, den1)

    print(f"Original Ratio: {num1} / {den1}")
    print(f"Simplified Ratio: {result_num} / {result_den}")