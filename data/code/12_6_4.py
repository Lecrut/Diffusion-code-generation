import math

def simplify_weight_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Returns a simplified weight ratio as (numerator, denominator).
    
    Handles potential zero inputs gracefully by returning the input pair unchanged
    if either is zero to avoid division-by-zero scenarios in downstream logic.
    Assumes integer inputs representing weights or counts.
    
    Args:
        numerator: The top value of the ratio.
        denominator: The bottom value of the ratio.
        
    Returns:
        A tuple (a, b) such that a/b is mathematically equivalent to n/d and gcd(a,b)=1.
    """
    if numerator == 0 or denominator == 0:
        return numerator, denominator
    
    common = math.gcd(numerator, denominator)
    
    simplified_numerator = numerator // common
    simplified_denominator = denominator // common
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    test_cases = [
        (10, 20),
        (5, 3),
        (0, 7),
        (8, 0),
        (-4, 6)
    ]

    for n, d in test_cases:
        result = simplify_weight_ratio(n, d)
        print(f"Ratio {n}:{d} simplified to {result[0]}:{result[1]}")