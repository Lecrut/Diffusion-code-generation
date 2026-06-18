import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculate the simplified form of a weight ratio (w1:w2).
    
    Handles potential zero inputs gracefully by returning the input values unchanged.
    Returns a tuple (simplified_w1, simplified_w2).

    Args:
        w1 (int): The first weight value.
        w2 (int): The second weight value.

    Returns:
        tuple[int, int]: A tuple containing the simplified weights as integers.
    """
    if w1 == 0 or w2 == 0:
        return w1, w2
    
    common_divisor = math.gcd(w1, w2)
    
    simplified_w1 = w1 // common_divisor
    simplified_w2 = w2 // common_divisor
    
    return simplified_w1, simplified_w2

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    samples = [
        (30, 45),   # Expected: (2, 3)
        (7, 8),     # Expected: (7, 8) - coprime
        (100, 0),   # Expected: (100, 0) - zero handling
        (0, 50),    # Expected: (0, 50) - zero handling
        (-4, 6),    # Negative input test -> Expected: (-2, 3)
    ]

    for w1_val, w2_val in samples:
        result = simplify_weight_ratio(w1_val, w2_val)
        print(f"Ratio {w1_val}:{w2_val} simplified to {result[0]}:{result[1]}")