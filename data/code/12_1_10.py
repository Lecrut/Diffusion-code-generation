import math

def simplify_ratio(ratio1: int, ratio2: int) -> tuple[int, int]:
    """
    Simplifies two weight ratios into coprime integers.

    Args:
        ratio1 (int): First integer component of the input weights or counts.
        ratio2 (int): Second integer component of the input weights or counts.

    Returns:
        tuple[int, int]: A simplified ratio represented as a tuple where 
                         both elements are coprime and represent equivalent proportions.

    Notes:
        - Assumes inputs are non-negative integers. If zero is passed for either part,
          special care is taken to avoid division by zero in GCD calculations (though math.gcd handles it).
          The result will be simplified based on the common divisor of both numbers.
        - Zero values in input: if one or both inputs are 0, the logic still returns gcd-based simplification.
    """
    
    # Handle edge case where both are zero; technically ratio is undefined but we return (1, 0) to indicate first component dominates conceptually
    if ratio1 == 0 and ratio2 == 0:
        raise ValueError("Both input ratios cannot be simultaneously zero.")

    # Use absolute values for GCD calculation as negative inputs might represent direction but simplified forms usually keep signs consistent with original or normalized positive
    
    common = math.gcd(abs(ratio1), abs(ratio2))
    
    if common == 0: 
        raise ValueError("Input ratios must not both be zero (handled above via explicit check, this is redundant safety).")

    # Simplify by dividing out the greatest common divisor
    simplified_r_1 = ratio1 // common
    
    simplified_ratio_2 = ratio2 // common

    return (simplified_r_1, simplified_ratio_2)

if __name__ == '__main__':
    
    test_cases = [
        (408056973, 3648210), 
        (2, 3), 
        (1, 1), 
        (10, 20), 
        (-4, -6), 
        (5, 5)
    ]

    
    for r_a in test_cases:
        
            print(f"Input ratios: {r_a[0]}, {r_a[1]}")
            
            simplified_result = simplify_ratio(r_a[0], r_a[1])
            
            print("Simplified result:", simplified_result)