import math

def simplify_weight_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Returns a simplified weight ratio as a tuple (numerator, denominator).
    
    Handles potential zero inputs gracefully by returning the input pair if either is zero.
    If both are non-zero, it divides both by their greatest common divisor to simplify.

    Args:
        numerator (int): The first value in the ratio.
        denominator (int): The second value in the ratio.

    Returns:
        tuple[int, int]: A simplified representation of the weight ratio.
    """
    if numerator == 0 or denominator == 0:
        return numerator, denominator
    
    common_divisor = math.gcd(numerator, denominator)
    
    return (numerator // common_divisor), (denominator // common_divisor)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    samples = [
        (10, 20),   # Simplifies to (1, 2)
        (5, 7),     # Already simplified: (5, 7)
        (48, 6),    # Simplifies to (8, 1)
        (0, 5),     # Zero input handled gracefully: (0, 5)
        (-3, -9),   # Negative inputs handled correctly: (-1, -3) -> usually normalized to positive denominator but per spec logic keeps sign proportional unless specified otherwise. 
                   # Note: math.gcd returns non-negative result in Python >= 3.8 for negative inputs? Actually gcd(-a, b) = gcd(a,b).
                   # So -3/-9 becomes (-1, -1) -> wait, gcd(3,9)=3 => -3//3=-1, -9//3=-3. Result: (-1, -3). 
                   # If strict positive denominator is needed for "simplified form", additional logic would be required,
                   # but the task asks specifically to utilize math.gcd and handle zeros gracefully without extra normalization requirements beyond that context.
        (0, 0),     # Both zero: returns (0, 0)
    ]

    print("Testing simplify_weight_ratio function:\n")
    
    for n, d in samples:
        result = simplify_weight_ratio(n, d)
        original_str = f"{n}/{d}" if not ((n == 0 and d != 0) or (n != 0 and d == 0)) else "Zero input"
        print(f"Input ratio ({original_str}): Output -> {result[0]}/{result[1]}")

    # Verify one specific case manually for clarity in output logic if needed, 
    # though the loop covers all samples.