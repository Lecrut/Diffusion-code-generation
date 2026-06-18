import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a coprime integer pair (a, b).
    
    The function converts the input floats to integers by scaling them up 
    if necessary to avoid floating-point precision issues during GCD calculation.
    It then divides both numbers by their greatest common divisor (GCD) 
    and returns the simplified tuple as positive integers. If inputs are zero or negative,
    they are treated as absolute values for simplification purposes while preserving sign logic 
    if strictly required; here we assume non-negative weights based on typical ratio usage.

    Args:
        ratio1 (float): First weight ratio value.
        ratio2 (float): Second weight ratio value.

    Returns:
        tuple[int, int]: A simplified coprime pair representing the ratio of inputs.
    
    Raises:
        ValueError: If both ratios are zero or if one is non-zero and the other is NaN/Inf.
    """
    # Handle edge cases where input might be invalid (NaN, Inf)
    def validate_input(val):
        return not math.isnan(val) and not math.isinf(val)

    if not all(validate_input(ratio1), validate_input(ratio2)):
        raise ValueError("Input ratios must be finite numbers.")

    # If both are zero, return (0, 0) as it's the only valid representation for undefined ratio
    if ratio1 == 0 and ratio2 == 0:
        return (0, 0)

    # Convert to integers by scaling up based on a common denominator approach or direct rounding
    # To ensure precision with floats like 3.5/7.0 -> 1/2, we can scale both to same integer base first
    # A robust way is to treat them as fractions: find LCM of denominators if they were explicit, 
    # but since inputs are raw floats, we'll use a large multiplier or direct GCD on scaled integers.

    # Scale up to avoid float inaccuracies during comparison/division
    scale_factor = 10**6  # Sufficient for most practical floating point ratios
    
    int_r1 = round(ratio1 * scale_factor)
    int_r2 = round(ratio2 * scale_factor)

    if int_r1 == 0 and int_r2 == 0:
        return (0, 0)

    # Compute GCD of the scaled integers
    common_divisor = math.gcd(int_r1, int_r2)

    simplified_a = abs(int_r1 // common_divisor)
    simplified_b = abs(int_r2 // common_divisor)

    # Ensure positive result; if original signs mattered differently, adjust here. 
    # Assuming weights are non-negative magnitudes:
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (10.5, 21.0),      # Expected: (378496, 756992) -> simplified to (1/2 scaled up? Let's trace logic manually below)
                          # Actually with scale=1e6: 
                          # int_r1 = 10500000, int_r2 = 21000000
                          # gcd(10500000, 21000000) = 10500000 -> (1, 2)
        (3.75, 4.5),       # Expected: (3/4 scaled? Let's trace)
                          # int_r1=3750000, int_r2=4500000
                          # gcd(3750000, 4500000)=75000 -> (50, 60) -> simplify further? No, GCD handles it.
                          # Wait: gcd(3750000, 4500000): 
                          # 3750000 = 12 * 312500; 4500000 = 18 * 250000
                          # Actually gcd(3.75e6, 4.5e6) -> divide by 75000 gives (50, 60)? 
                          # Let's recompute: 3.75/4.5 = 375/450 = 15/18 = 5/6
                          # So expected output should be (5, 6) if scaled correctly.
        (2.0, 4.0),        # Expected: (1, 2)
        (1.0, 3.0),        # Expected: (1, 3)
    ]

    for r1, r2 in test_cases:
        result = simplify_ratio(r1, r2)
        print(f"Ratio {r1} : {r2} -> Simplified ({result[0]}, {result[1]})")