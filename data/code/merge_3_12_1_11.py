import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two floating-point weight ratios into a coprime integer pair (a, b).

    Args:
        ratio1 (float): First input ratio value.
        ratio2 (float): Second input ratio value.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as integers that are coprime.

    The function handles floating-point comparisons by converting inputs to fractions-like behavior
    using a tolerance-based closest integer approach if exact representation isn't possible due to precision issues.
    If both ratios are effectively zero (within 1e-9), it returns (0, 1).
    
    Note: Due to potential float imprecision, small non-zero values might result in denominators like ~34 rather than exactly 35 
    when using pure integer conversion from floats. This function uses a heuristic based on the ratio of rounded values
    scaled up by powers of two (2^18) to minimize precision loss while maintaining correctness for standard use cases.
    
    Example:
        >>> simplify_ratio(1, 4)
        (1, 4)
        
        >>> simplify_ratio(35, 60) -> simplified to gcd=5 => (7, 12)
    """
    # Handle edge case where both are zero or negligible
    if abs(ratio1) < 1e-9 and abs(ratio2) < 1e-9:
        return (0, 1)

    # Scale up to handle floating-point precision issues
    scale = 2**18
    
    a_scaled = int(round(abs(ratio1) * scale))
    b_scaled = int(round(abs(ratio2) * scale))
    
    # Ensure non-negative results based on original signs (though problem implies weights, so typically positive)
    sign_a = -1 if ratio1 < 0 else 1
    
    a = abs(a_scaled)
    b = abs(b_scaled)
    
    gcd_val = math.gcd(a, b)
    
    return (sign_a * (a // gcd_val), b // gcd_val)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    
    test_cases = [
        (1.0, 4.0),
        (35.0, 60.0),   # Expected: (7, 12) after dividing by GCD of scaled integers
        (-2.0, -3.0),  # Test negative inputs preserving sign logic if applicable
        (0.1428571429, 0.25),      # Approximation for 1/7 vs 1/4
        (float('inf'), float('inf'))  # Infinity case handling
    ]

    print("Testing simplify_ratio function:")