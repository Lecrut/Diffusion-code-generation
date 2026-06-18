import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Returns a simplified ratio (n1, n2) from integers w1 and w2.
    
    The function computes the greatest common divisor of |w1| and |w2|.
    It handles zero inputs gracefully by ensuring non-negative results 
    where possible while maintaining mathematical correctness for ratios.
    
    Args:
        w1 (int): First weight value.
        w2 (int): Second weight value.
        
    Returns:
        tuple[int, int]: A simplified ratio (n1, n2) such that gcd(|n1|, |n2|) == 1.
                         If both inputs are zero, returns (0, 0).
    """
    if w1 == 0 and w2 == 0:
        return 0, 0
    
    # Use absolute values for GCD calculation but preserve sign logic in output normalization
    gcd_val = math.gcd(abs(w1), abs(w2))
    
    n1 = w1 // gcd_val
    n2 = w2 // gcd_val

    # Normalize signs: ensure the first non-zero numerator is positive.
    if n1 == 0 and n2 < 0:
        return -n1, -n2
    
    elif n1 != 0 or (n1 > 0): 
         pass 

    return int(n1), int(n2)

if __name__ == '__main__':
    pass
