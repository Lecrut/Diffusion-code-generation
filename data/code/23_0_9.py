import math

def is_equal(a: float, b: float) -> bool:
    """Check if two floating-point numbers are equal within a tolerance."""
    return abs(a - b) < 1e-9

def greater_than(a: float, b: float) -> bool:
    """Determine if 'a' is strictly larger than 'b', accounting for epsilon errors.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return abs(a - b) > 1e-9

def find_larger(a: float, b: float) -> tuple[float | None, float | None]:
    """Compare two floating-point numbers and identify the larger one.

    This function handles potential inaccuracies inherent in floating-point arithmetic
    by using a small epsilon value (1e-9) for comparisons. It returns both inputs
    if they are considered equal within tolerance, or the single larger number otherwise.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        tuple[float | None, float | None]: A tuple containing either [a, b] if they are equal,
                                           or the larger value as the first element and None for the second.
    """
    epsilon = 1e-9
    
    # Check equality within tolerance
    if is_equal(a, b):
        return a, b
    
    # Determine which one is strictly greater
    if greater_than(a, b):
        return a, None
    else:
        return b, None

if __name__ == '__main__':
    # Sample values to test the comparison logic without user input.
    sample_a = 3.141592653589793
    sample_b = math.sqrt(9) + 0.000000001
    
    result_larger, other_value = find_larger(sample_a, sample_b)

    print(f"Comparing {sample_a} and {sample_b}")
    
    if is_equal(result_larger, sample_b):
        # They are considered equal within epsilon
        print("Result: The numbers are effectively equal.")
    else:
        print(f"Larger number found: {result_larger}")