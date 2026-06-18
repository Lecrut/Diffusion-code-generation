import math
from typing import List, Tuple

def simplify_ratio(numerator: int, denominator: int) -> float:
    """
    Simplify a ratio of two integers into their greatest common divisor normalized form.
    
    Args:
        numerator (int): The top value of the ratio.
        denominator (int): The bottom value of the ratio.
        
    Returns:
        float: The simplified ratio as n/d where gcd(n, d) = 1 and signs are handled correctly.
             If both inputs have a common divisor > 0, it divides them by that GCD.
             Handles negative numbers by ensuring the denominator is positive (standard convention).
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both numerator and denominator must be integers.")

    # Handle zero cases
    if denominator == 0:
        return float('inf') if numerator != 0 else 1.0
    
    g = math.gcd(abs(numerator), abs(denominator))
    
    simplified_n = numerator // g
    simplified_d = denominator // g
    
    # Standardize sign so that the denominator is positive (unless it's zero, handled above)
    if simplified_d < 0:
        simplified_n *= -1
        simplified_d *= -1
        
    return simplified_n / simplified_d

def process_ratio_pairs(pairs: List[Tuple[int, int]]) -> List[float]:
    """
    Accepts a list of length pairs and returns a list of simplified ratios.
    
    Args:
        pairs (List[Tuple[int, int]]): A list where each element is a tuple representing 
                                        the numerator and denominator of a ratio pair.
                                        
    Returns:
        List[float]: A list containing the simplified float values for all input pairs.
                     If any division by zero occurs in the original data, it returns infinity or 1.0 accordingly.
    
    Raises:
        ValueError: If an element is not a valid tuple of two integers.
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    result = []
    for i, pair in enumerate(pairs):
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            raise ValueError(f"Invalid pair at index {i}: expected tuple/list of two integers, got {pair}")
        
        n, d = int(pair[0]), int(pair[1])
        result.append(simplify_ratio(n, d))

    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_pairs: List[Tuple[int, int]] = [
        (4, 8),   # Should simplify to 0.5
        (-2, -6), # Should simplify to 1/3 -> ~0.333...
        (7, 35),  # Should simplify to 0.2
        (9, 0),   # Division by zero case -> inf or similar handling based on logic above
        (-18, -4) # Simplifies to 9/2 = 4.5
    ]

    simplified_ratios = process_ratio_pairs(sample_pairs)

    print("Original pairs and their simplified ratios:")
    for i, (original_pair, ratio_value) in enumerate(zip(sample_pairs, simplified_ratios)):
        print(f"Pair {i+1}: {original_pair} -> Ratio: {ratio_value}")