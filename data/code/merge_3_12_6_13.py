import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculate the simplified form of a weight ratio (w1:w2).
    
    Handles potential zero inputs gracefully by returning the input values 
    if either is zero. If both are non-zero, it divides both by their GCD.

    Args:
        w1 (int): The first part of the weight ratio.
        w2 (int): The second part of the weight ratio.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    
    Examples:
        >>> simplify_weight_ratio(4, 6)
        (2, 3)
        >>> simplify_weight_ratio(0, 5)
        (0, 5)
        >>> simplify_weight_ratio(10, 0)
        (10, 0)
    """
    if w1 == 0 or w2 == 0:
        return w1, w2
    
    common_divisor = math.gcd(w1, w2)
    
    simplified_numerator = w1 // common_divisor
    simplified_denominator = w2 // common_divisor
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (4, 6),
        (10, 5),
        (7, 28),
        (0, 9),
        (-3, -6)
    ]

    print("Testing simplify_weight_ratio function:\n")
    
    for w1, w2 in samples:
        result = simplify_weight_ratio(w1, w2)
        original_str = f"{w1}:{w2}" if not (w1 == 0 or w2 == 0) else f"{w1}:{w2} (zero input)"
        simplified_str = f"{result[0]}:{result[1]}"
        print(f"Input: {original_str}")
        print(f"Simplified Ratio: {simplified_str}\n")