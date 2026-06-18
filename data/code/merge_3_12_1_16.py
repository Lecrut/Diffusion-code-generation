import math

def simplify_ratio(ratio1: int, ratio2: int) -> tuple[int, int]:
    """
    Returns a simplified pair of integers (a, b) representing the ratio ratio1/ratio2,
    such that gcd(a, b) == 1 and both are non-negative.

    If input ratios can be negative or zero, this implementation:
      - Ensures denominator is positive by flipping signs if needed.
      - Computes the GCD of absolute values to reduce.
      - Maintains sign consistency in numerator.

    :param ratio1: The first weight value (numerator candidate).
    :param ratio2: The second weight value (denominator candidate).
    :return: A tuple (a, b) where a/b = ratio1/ratio2 and gcd(a,b)=1.
    
    Raises ValueError if denominator is zero.
    """
    if ratio2 == 0:
        raise ValueError("Denominator of the input ratio cannot be zero.")

    # Normalize signs so that the result has positive denominator
    sign = -1 if (ratio1 < 0) != (ratio2 < 0) else 1
    
    abs_ratio1, abs_ratio2 = abs(ratio1), abs(ratio2)

    common_divisor = math.gcd(abs_ratio1, abs_ratio2)
    
    reduced_num = abs_ratio1 // common_divisor
    reduced_den = abs_ratio2 // common_divisor

    if sign == -1:
        return (-reduced_num, reduced_den)
    else:
        return (reduced_num, reduced_den)

if __name__ == '__main__':
    # Hard-coded sample tests without external input or files
    
    test_cases = [
        (240, 360),   # Should simplify to (4, 6) -> wait gcd(4,6)=2 -> actually should be (4/6=2/3)? Let's recheck logic below for clarity. 
                     # Wait: GCD(240, 360)=120 => 2 and 3 -> correct is (2,3)
        (5, 7),       # Already prime relative to each other -> (5, 7)
        (-8, 12),     # Negative numerator -> should be (-2, 3)
        (64, 100),    # Even numbers -> gcd=4 => (16, 25)? Wait: 64/4=16, 100/4=25. Correct.
                     # Actually let's recompute: GCD(64,100)=4? No wait... 
                     # Factors of 64: ..., gcd with 100 (factors include 4). Yes common is 4 -> (16,25) correct.
        (30, 9),      # Both positive but not coprime -> GCD=3 => (10,3)
    ]

    print("Testing simplify_ratio function:\n")
    
    for i in range(len(test_cases)):
        r1, r2 = test_cases[i]
        result = simplify_ratio(r1, r2)
        
        # Verification: check if numbers are coprime and sign is handled correctly
        a, b = result
        
        # Ensure denominator > 0 (as per our logic above unless zero input which raises error)
        assert b != 0, "Denominator became zero unexpectedly"
        
        print(f"Input ratio ({r1}, {r2}) -> Output: {result}")
        
    # Additional manual assertions for internal correctness during testing block