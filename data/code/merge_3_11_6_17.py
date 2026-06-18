import math

def calculate_ratio_simplified(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two integers by dividing both 
    by their Greatest Common Divisor (GCD).

    Args:
        numerator (int): The first integer.
        denominator (int): The second integer.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    
    Note: Handles negative numbers correctly to ensure positive GCD behavior 
         while preserving sign conventions consistent with mathematical simplification.
    """
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    # Ensure we work with absolute values for GCD calculation
    abs_num = abs(numerator)
    abs_den = abs(denominator)

    gcd_value = math.gcd(abs_num, abs_den)

    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value

    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_cases = [
        (-180, -36),      # Both negative -> both positive in result
        (42, 7),          # Simple division
        (999999999999999999, 5) ,# Large integers to test robustness with Python's arbitrary precision support implicitly handled via integer arithmetic.
    ]

    for n, d in test_cases:
        result = calculate_ratio_simplified(n, d)
        print(f"Ratio of {n} / {d}: {result[0]} / {result[1]}")