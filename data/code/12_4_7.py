import math
from typing import List, Tuple

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of two integers."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_ratio(ratio_tuple: Tuple[int, int]) -> List[int]:
    """Simplify a single weight ratio tuple by dividing both parts by their GCD.
    
    Args:
        ratio_tuple: A tuple or list of two integers representing the ratio (a:b).
        
    Returns:
        A new list containing the simplified [a, b].
        
    Examples:
        >>> simplify_ratio((24, 36))
        [2, 3]
        >>> simplify_ratio((-10, -5))
        [-2, -1]
        >>> simplify_ratio((7, 1))
        [7, 1]
    """
    a = int(ratio_tuple[0])
    b = int(ratio_tuple[1])
    
    common_divisor = gcd(a, b)
    
    return [a // common_divisor, b // common_divisor]

def simplify_weight_ratios(weights: List[Tuple[int, int]]) -> List[List[int]]:
    """Process a list of weight ratio tuples and return simplified lists.
    
    This function iterates through each ratio in the input list, simplifies it 
    by dividing both numerator and denominator by their greatest common divisor (GCD),
    and returns a new list containing only these simplified results.

    Args:
        weights: A list of tuples/lists representing weight ratios [a:b].
        
    Returns:
        A list where each element is the simplified ratio as a two-element list.
    """
    return [simplify_ratio(r) for r in weights]

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files.
    raw_ratios = [
        (24, 36),   # Should simplify to [2, 3]
        (-10, -5),  # Should simplify to [-2, -1]
        (7, 8),     # Already simplified -> [7, 8]
        (15, 0) if False else (15, 45), # Invalid case handled by logic: GCD(15,45)=15 -> [1,3]
    ]

    # Fix the third item for clarity in this specific run context to ensure valid math operations.
    raw_ratios[2] = (7, 8) 

    result_lists = simplify_weight_ratios(raw_ratios)
    
    print(f"Input Ratios: {raw_ratios}")
    print("Simplified Results:")
    for i, ratio in enumerate(result_lists):
        simplified_str = f"[{ratio[0]}, {ratio[1]}]" if len(ratio) == 2 else str(ratio)
        # Note: Logic ensures two integers are always returned. 
        original_input_display = f"({raw_ratios[i][0]}, {raw_ratios[i][1]})"
        print(f"{original_input_display} -> {simplified_str}")

    # Additional verification block to ensure no runtime errors occurred with internal logic.
    assert result_lists[0] == [2, 3], "First ratio simplification failed."
    assert result_lists[1] == [-2, -1], "Second negative ratio simplification failed."
    assert result_lists[2] == [7, 8], "Third already simplified ratio check failed."
    
    print("\nAll verifications passed.")