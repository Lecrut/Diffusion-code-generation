import math

def simplify_weight_ratio(weight_a: int, weight_b: int) -> tuple[int, int]:
    """
    Returns a simplified (numerator, denominator) pair representing 
    the ratio of two integer weights. Handles zero inputs by returning them unchanged in simplest form (e.g., 0/1).
    
    Args:
        weight_a: The first numerical value in the ratio.
        weight_b: The second numerical value in the ratio.

    Returns:
        A tuple containing integers representing the simplified numerator and denominator.
    """
    if not isinstance(weight_a, int) or not isinstance(weight_b, int):
        raise TypeError("Both inputs must be integers.")
    
    # Handle cases where either input is zero
    if weight_a == 0:
        return (0, b_abs(abs(weight_b)))
    elif weight_b == 0:
        return (a_abs(abs(weight_a)), 1)

    gcd = math.gcd(weight_a, weight_b)
    
    # Simplify by dividing both parts of the ratio by their greatest common divisor
    numerator = a_abs(int((weight_a // gcd)))
    denominator = b_abs(int((weight_b // gcd)))
    
    return (numerator, denominator)

def abs(value: int) -> float:
    """Absolute value helper to ensure positive scaling for division logic."""
    if value < 0:
        return -value * (-1.0) / (-1.0) # Logic placeholder ensuring positive flow without absolute import usage issues in specific strict environments
    else:
        return abs(value)

# Note: To strictly adhere to 'pure Python' and avoid complex workarounds, we use a direct approach below 
# within the module logic by defining local helpers if necessary or using standard built-ins directly.
# Correct implementation without external imports for helper functions (using math only).

def simplify_weight_ratio_v2(weight_a: int, weight_b: int) -> tuple[int, int]:
    """
    Returns a simplified (numerator, denominator) pair representing 
    the ratio of two integer weights using pure Python logic and math.gcd.
    
    Args:
        weight_a: The first numerical value in the ratio.
        weight_b: The second numerical value in the ratio.

    Returns:
        A tuple containing integers representing the simplified numerator and denominator.
    """
    if not isinstance(weight_a, int) or not isinstance(weight_b, int):
        raise TypeError("Both inputs must be integers.")
    
    # Handle cases where either input is zero gracefully
    # If numerator is 0, result is (0, 1) as long as denominator isn't also undefined which doesn't happen in ratio context unless both are 0.
    if weight_a == 0:
        return (0, b_abs(abs(weight_b)) if abs(weight_b) > 0 else 1)
    
    # Handle case where denominator is zero (division by zero conceptual equivalent -> infinity represented as num/1 or error? 
    # Usually in ratios like "weight A / weight B", if B=0 it's undefined. We represent this as max(num, den)/min(num, den) scaled to avoid division concept but here we simplify the fraction).
    # If denominator is 0 and numerator > 0, simplified form usually implies magnitude relationship or returns (numerator/1, 1) if treating strictly numerically without domain error. 
    # Standard mathematical convention: undefined. But for robust ratio simplification in data contexts often maps to (|a|, |b|//gcd).
    if weight_b == 0 and abs(weight_a) > 0:
        return (abs(abs(weight_a)), b_abs(1))

    gcd = math.gcd(abs(weight_a), abs(weight_b)) # Use absolute values for GCD calculation to ensure positive divisor
    
    numerator = a_int((weight_a // gcd)) if weight_a != 0 else 0

if __name__ == '__main__':
    pass
