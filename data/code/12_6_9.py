import math

def simplify_weight_ratio(weight1: int, weight2: int) -> tuple[int, int]:
    """
    Calculates the simplified form of a single weight ratio (weight1 : weight2).
    
    Args:
        weight1 (int): The first weight value.
        weight2 (int): The second weight value.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator 
                         of the simplified fraction after dividing both by their GCD.
                         
    Handles potential zero inputs gracefully by returning a ratio where at least one part is non-zero,
    or [0, 1] if both are zero (representing an undefined but safe state).
    """
    # Handle case where both weights are zero to avoid division by zero in logic flow later.
    if weight1 == 0 and weight2 == 0:
        return 0, 1
    
    # Calculate the Greatest Common Divisor
    common_divisor = math.gcd(weight1, weight2)
    
    # Simplify the ratio by dividing both parts by their GCD
    simplified_numerator = weight1 // common_divisor
    simplified_denominator = weight2 // common_divisor
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        (10, 5),      # Standard case: should result in (2, 1)
        (8, 4),       # Another standard case: should result in (2, 1)
        (7, 3),       # Irreducible fraction: should remain (7, 3)
        (-6, -9),     # Negative inputs: should handle signs correctly -> (-2, -3) or equivalent logic depending on GCD sign handling. 
                     # Note: math.gcd returns non-negative in Python 3.8+, so negatives will be divided out to become positive denominators usually if we strictly follow standard fraction rules,
                     # but here we just divide by the absolute gcd magnitude found by math.gcd which is always >=0.
                     # Let's trace -6 // 3 = -2, -9 // 3 = -3. Result (-2, -3). This preserves sign relationship.
        (5, 0),       # Zero denominator input: should result in (1, 0) conceptually if we treat it as a ratio where second is zero? 
                     # Actually math.gcd(5,0)=5. 5//5=1, 0//5=0 -> (1, 0).
        (0, 8),       # Zero numerator input: should result in (0, 1)
    ]

    print("Weight Ratio Simplification Results:")
    for w1, w2 in test_cases:
        simplified = simplify_weight_ratio(w1, w2)
        original_str = f"{w1}:{w2}" if not (simplified[0] == 0 and simplified[1] == 0) else "Undefined" # Avoid printing undefined as a ratio string to prevent confusion with division by zero logic in display. 
        print(f"Original Ratio ({original_str}): Simplified -> {simplified}")