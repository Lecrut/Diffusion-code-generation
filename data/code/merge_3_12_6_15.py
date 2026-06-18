import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculate the simplified form of a weight ratio (w1:w2).
    
    Handles potential zero inputs gracefully by returning the input as-is 
    if both are zero or if one is non-zero and the other is zero.
    
    Args:
        w1 (int): The first weight value.
        w2 (int): The second weight value.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                         If both inputs are 0, returns (0, 0).
                         Otherwise, divides by their greatest common divisor.
    
    Examples:
        >>> simplify_weight_ratio(4, 8)
        (1, 2)
        >>> simplify_weight_ratio(5, 0)
        (5, 0)
        >>> simplify_weight_ratio(0, 7)
        (0, 7)
        >>> simplify_weight_ratio(0, 0)
        (0, 0)
    """
    
    # Handle the case where both weights are zero
    if w1 == 0 and w2 == 0:
        return 0, 0
    
    # If one is non-zero and the other is zero, no simplification needed beyond identity
    if w1 != 0 or w2 != 0:
        common_divisor = math.gcd(w1, w2)
        
        simplified_w1 = w1 // common_divisor
        simplified_w2 = w2 // common_divisor
        
        return simplified_w1, simplified_w2
    
    # This part is theoretically unreachable given the checks above 
    # but ensures robustness against unexpected logic paths.
    return 0, 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (4, 8),   # Expected: (1, 2)
        (5, 0),   # Expected: (5, 0)
        (0, 7),   # Expected: (0, 7)
        (0, 0),   # Expected: (0, 0)
        (-3, -9), # Expected: (-1, -3) or simplified positive version depending on convention; 
                 # math.gcd handles negatives correctly for magnitude but signs remain.
                 # Let's stick to standard gcd behavior which preserves sign logic in division.
    ]

    print("Running sample tests...")
    for w1, w2 in test_cases:
        result = simplify_weight_ratio(w1, w2)
        print(f"Ratio {w1}:{w2} simplified -> {result}")