import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculate the simplified form of a weight ratio (w1:w2).
    
    Handles potential zero inputs gracefully by returning the input pair if both are non-zero.
    If one is zero and the other is not, it returns the same value paired with 0 or vice versa.
    If both are zero, it returns (0, 0) as no meaningful ratio exists.
    
    The function uses math.gcd to reduce the fraction w1/w2 by their greatest common divisor.
    
    Args:
        w1 (int): First weight value.
        w2 (int): Second weight value.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator weights.
    """
    if w1 == 0 and w2 == 0:
        return 0, 0
    
    common = math.gcd(w1, w2)
    
    # Ensure we handle negative numbers correctly by keeping signs consistent with input or standard convention (positive first)
    # Standard mathematical practice often keeps the denominator positive. If original was (-5:-3), result is -5/-3 -> 5/3? 
    # Or does it preserve sign of numerator? Let's assume preservation of relative sign but normalized magnitude.
    # A common approach for ratios: if both negative, make them positive. If one negative, keep the first as reference or normalize to positive denominator.
    # Given "simplified form", usually implies smallest integers with same sign relationship. 
    # However, standard fraction simplification often prefers positive denominator. Let's stick to preserving signs but dividing by gcd magnitude.
    
    simplified_numerator = w1 // common
    simplified_denominator = w2 // common
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    samples = [
        (40, 60),   # Should simplify to 2:3
        (-15, -9),  # Both negative, should likely be -(-5):-(3) -> -5:-3? Or normalized to positive? 
                   # Let's output the direct division result which maintains relative signs.
                    # Actually, standard simplification usually makes denominator positive if possible.
                    # But without specific instruction on sign convention for negatives, we will just divide by gcd(|a|, |b|) and apply original signs logic implicitly via integer division? 
                    # No, math.gcd returns non-negative. So -15 // 3 = -5. Correct.
        (0, 2),     # Zero numerator -> should remain 0:2 or simplified to 0:1? Usually ratios imply non-zero denominator contextually but strictly 0/2 is 0:1 in value. 
                   # The prompt says "handle potential zero inputs gracefully". 
                   # If w1=0, gcd(0, x) = x. So 0//x = 0, x//x = 1. Result (0, 1). This seems most logical for a ratio representation of value 0 vs something else.
        (-4, -8),   # Both negative -> -1:-2? Or normalized to positive? Let's stick to the math operation result: gcd(4,8)=4 => -1, -2.
                   # If we want strictly positive denominator convention for ratios like fractions: 
                   # We can adjust here if needed, but pure division is safest unless specified otherwise.
        (7, 0),     # Non-zero numerator, zero denominator -> undefined ratio mathematically? 
                   # gcd(7, 0) = 7. Result 1, 0. This represents an infinite slope or similar concept in discrete steps.
    ]

    print("Sample Weight Ratio Simplifications:")
    for w1, w2 in samples:
        result_numerator, result_denominator = simplify_weight_ratio(w1, w2)
        # Format output nicely
        if result_denominator == 0 and result_numerator != 0:
            ratio_str = f"{result_numerator}:inf"
        else:
            ratio_str = f"{result_numerator}:{result_denominator}"
        
        original_ratio_str = f"{w1}:{w2}"
        print(f"Original ({original_ratio_str}) -> Simplified ({ratio_str})")