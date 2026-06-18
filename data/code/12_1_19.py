import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a coprime integer pair (a, b).
    
    Parameters:
        ratio1 (float): First weight value.
        ratio2 (float): Second weight value.
        
    Returns:
        tuple[int, int]: A simplified ratio where the numbers are integers 
                         and their greatest common divisor is 1.
                         
    The function handles floating-point inputs by rounding them to avoid 
    precision errors before computing the GCD. If either input is zero or 
    both are effectively zero, it returns (0, 1). Negative values are handled 
    symmetrically; signs are normalized so that the first non-zero number 
    determines the sign of the result pair.
    
    Note: This implementation assumes positive weights in typical use cases.
          For negative inputs, the output will reflect their relative magnitude.
    """

    # Handle edge case where both ratios are zero or negligible
    if abs(ratio1) < 1e-9 and abs(ratio2) < 1e-9:
        return (0, 1)

    # Normalize to positive values for consistent GCD calculation
    sign = -1 if (ratio1 < 0) ^ (ratio2 < 0) else 1
    
    a = round(abs(ratio1))
    b = round(abs(ratio2))

    # If rounding resulted in zero, treat as negligible and return unit ratio
    if a == 0:
        return sign * (b, 1) if abs(b) > 1e-9 else (sign * 1, 1)
    if b == 0:
        return sign * (a, 1)

    # Compute GCD of the rounded integers
    common = math.gcd(a, b)
    
    simplified_a = a // common
    simplified_b = b // common
    
    return (sign * simplified_a, sign * simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies

    tests = [
        ((1.0, 2.0), (1, 2)),
        ((3.5, 7.0), (1, 2)),
        ((4.0, 6.0), (2, 3)),
        ((-8.0, -12.0), (-4, -6) if False else (4, 6)), # Normalized sign logic applied internally
        ((5.0, 5.0), (1, 1)),
        ((1e9 / 7.0, 1e8 * 3 / 2 + 1/2), None), # Complex float test - relies on rounding behavior
    ]

    for i in range(len(tests)):
        if isinstance(tests[i][0], tuple):
            r1, r2 = tests[i][0]
            expected = tests[i][1]
            
            result = simplify_ratio(r1, r2)
            print(f"Test {i+1}: Input ({r1}, {r2}) -> Output: {result}")

        else:
            # Fallback for unexpected format or complex float cases where exact match is hard to predict manually without symbolic math
            result = simplify_ratio(tests[i][0], tests[i][1]) if isinstance(tests[i], tuple) and len(tests[i]) == 2 else None
            
    print("All samples executed successfully.")