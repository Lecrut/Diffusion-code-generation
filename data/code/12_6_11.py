import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculates the simplified form of a weight ratio (w1:w2).
    
    Handles potential zero inputs gracefully by returning the input values 
    if either is zero or both are non-zero but their GCD results in no change.
    
    Args:
        w1 (int): The first weight value.
        w2 (int): The second weight value.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    """
    if not isinstance(w1, int) or not isinstance(w2, int):
        raise TypeError("Both inputs must be integers.")

    # Handle cases where one of them is zero to avoid division by zero in GCD logic 
    # (though math.gcd handles 0 fine, it's good for clarity on ratio definition).
    if w1 == 0:
        return (0, abs(w2))
    if w2 == 0:
        return (abs(w1), 0)

    common_divisor = math.gcd(abs(w1), abs(w2))
    
    simplified_w1 = w1 // common_divisor
    simplified_w2 = w2 // common_divisor
    
    # Ensure the sign convention is consistent: if denominator is negative, 
    # move the sign to the numerator. If both are positive/negative as per standard ratio simplification.
    if simplified_w2 < 0:
        simplified_w1 *= -1
        simplified_w2 = abs(simplified_w2)

    return (simplified_w1, simplified_w2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (30, 45),   # Expected: (2, 3)
        (8, 16),    # Expected: (1, 2)
        (-9, -12),  # Expected: (-3, -4) -> normalized to (-3, -4) or logic dependent on sign handling above. 
                   # Based on code: gcd(9,12)=3 -> -3/-4 -> w2 is negative so flip signs -> (3, 4).
        (0, 5),     # Expected: (0, 5)
        (7, 0),     # Expected: (7, 0)
    ]

    print("Testing simplify_weight_ratio function:\n")
    
    for w1, w2 in samples:
        result = simplify_weight_ratio(w1, w2)
        ratio_str = f"{w1}:{w2}" if not isinstance(result[0], tuple) else "" # Just printing the input context here implicitly handled by loop
        
        print(f"Input Ratio ({w1}, {w2}) -> Simplified: {result}")

    # Additional explicit test case for clarity in output
    final_test = simplify_weight_ratio(6, 9)
    print(f"\nFinal Test (6:9) -> {final_test}")