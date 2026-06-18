import math

def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses a direct subtraction followed by an absolute value operation.
    For standard IEEE 754 double-precision floats (which Python natively supports),
    this approach is efficient and accurate for typical use cases involving weight calculations.

    Parameters:
        a (float): First floating-point number representing a weight or value.
        b (float): Second floating-point number representing another weight or value.

    Returns:
        float: The absolute difference between the two input values.
    
    Example:
        >>> calculate_weight_difference(10.5, 3.2)
        7.3
    
    Note:
        This implementation prioritizes readability and correctness over micro-optimizations
        that could introduce numerical instability (e.g., using bit-level manipulation).
        For extreme performance requirements in non-critical paths, inline usage is recommended.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    weight_a = 150.75
    weight_b = 49.23
    
    result = calculate_weight_difference(weight_a, weight_b)
    
    print(f"Absolute difference between {weight_a} and {weight_b}: {result}")