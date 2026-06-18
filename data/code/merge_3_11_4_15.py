import math
from typing import List, Tuple

def simplify_fraction(numerator: int, denominator: int) -> Tuple[int, int]:
    """Simplify a fraction by dividing both numerator and denominator by their GCD."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    # Handle negative denominators to ensure standard form (positive denominator)
    sign = -1 if denominator < 0 else 1
    
    abs_num = abs(numerator)
    abs_den = abs(denominator)
    
    common_divisor = math.gcd(abs_num, abs_den)
    
    simplified_numerator = numerator // common_divisor * sign
    simplified_denominator = (abs_den // common_divisor) if denominator < 0 else (abs_den // common_divisor)
    
    # Re-apply the original sign logic correctly for negative results with positive denominators
    if denominator < 0:
        return -simplified_numerator, abs(simplified_denominator) * (-1) if simplified_numerator > 0 else abs(simplified_numerator), abs(simplified_denominator)

    # Correct simplification ensuring standard form (positive denominator)
    gcd_val = math.gcd(abs(numerator), abs(denominator))
    
    return numerator // gcd_val, denominator // gcd_val

def get_simplified_ratios(pairs: List[Tuple[int, int]]) -> List[str]:
    """Accepts a list of length pairs and returns a list of simplified ratio strings."""
    ratios = []
    for num, den in pairs:
        if den == 0:
            raise ValueError(f"Invalid pair {num, den}: denominator cannot be zero.")
        
        s_num, s_den = simplify_fraction(num, den)
        # Format as "a/b", handling negative signs appropriately
        ratio_str = f"{s_num}/{abs(s_den)}" if s_den < 0 else f"{s_num}/{s_den}"
        ratios.append(ratio_str)
    
    return ratios

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    sample_pairs = [
        (12, 8),   # Should simplify to 3/2
        (-4, -6),  # Should simplify to 2/3
        (5, 0),    # Will raise an error as denominator is zero
        (7, 14),   # Should simplify to 1/2
        (0, 9)     # Should simplify to 0/9 -> 0/1 logic handled by gcd(0,x)=x
    ]

    try:
        result = get_simplified_ratios(sample_pairs)
        print("Simplified Ratios:")
        for i, ratio in enumerate(result):
            print(f"Pair {i+1}: {ratio}")
    except ValueError as e:
        # Specifically handling the zero denominator case from sample input (5, 0)
        if "denominator cannot be zero" in str(e):
            print("Error:", e)
        else:
            raise