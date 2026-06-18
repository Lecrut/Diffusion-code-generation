"""
Module to compare two floating-point numbers with epsilon-based tolerance.

This script defines a function that determines which of two floats is larger,
accounting for inherent precision errors in IEEE 754 double-precision arithmetic.
Instead of direct equality checks or strict inequality comparisons without context,
it uses a small threshold (epsilon) to define the range within which numbers
are considered effectively equal. If both numbers fall outside this difference,
the one with the greater absolute value is deemed larger.

Usage:
    Run as-is; no input required via CLI or stdin.
"""

def are_equal_with_epsilon(a: float, b: float, epsilon: float = 1e-9) -> bool:
    """Check if two floats are effectively equal within a tolerance."""
    return abs(a - b) <= epsilon

def is_greater_than_epsilon(a: float, b: float, epsilon: float = 1e-9) -> bool:
    """Determine if 'a' is strictly greater than 'b' considering floating-point noise.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        epsilon (float): Tolerance threshold for equality checks. Default is 1e-9.

    Returns:
        bool: True if 'a' > 'b', False otherwise.
    """
    return a - b > epsilon

def find_larger(a: float, b: float, epsilon: float = 1e-9) -> tuple[float | None, float]:
    """Compare two floats and identify the larger one or if they are equal within tolerance.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        epsilon (float): Tolerance threshold for equality checks. Default is 1e-9.

    Returns:
        tuple[float | None, float]: A tuple containing the larger value or None if equal,
                                   and the values that were compared.
    """
    l = a if are_equal_with_epsilon(a, b) else (a if is_greater_than_epsilon(a, b) else b)
    return l, a

if __name__ == '__main__':
    pass
