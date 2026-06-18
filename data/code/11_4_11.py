import math
from typing import List, Tuple

def simplify_ratio(a: int, b: int) -> str:
    """
    Simplifies a ratio of two integers into its lowest terms and returns it as a string.
    
    Args:
        a (int): The numerator or first element of the pair.
        b (int): The denominator or second element of the pair.
        
    Returns:
        str: A simplified ratio in the format "a:b". Handles negative numbers correctly.
             If both are zero, returns "0:0".
    """
    if a == 0 and b == 0:
        return "0:0"

    # Determine signs to handle negatives properly (e.g., -2:-4 -> -1:-2 or 1:2)
    # Convention: make the denominator positive, adjust numerator sign accordingly.
    common = gcd(abs(a), abs(b))
    
    simplified_a = a // common
    simplified_b = b // common

    if simplified_b < 0:
        # Make denominator positive by flipping signs of both parts
        return f"{-simplified_a}:{abs(simplified_b)}"
    else:
        return f"{simplified_a}:{simplified_b}"

def gcd(x: int, y: int) -> int:
    """Calculate the greatest common divisor using Euclidean algorithm."""
    while y != 0:
        x, y = y, x % y
    return abs(x)

def process_pairs(pairs: List[Tuple[int, int]]) -> List[str]:
    """
    Accepts a list of length pairs and returns a list of simplified ratios.

    Args:
        pairs (List[Tuple[int, int]]): A list where each element is a tuple (a, b).

    Returns:
        List[str]: A list containing the string representation of simplified ratios for each pair.
    """
    return [simplify_ratio(a, b) for a, b in pairs]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_pairs = [(2, 4), (-3, -9), (5, 0), (7, 14), (0, 8)]

    result_ratios = process_pairs(sample_pairs)

    print("Input Pairs:", sample_pairs)
    print("Simplified Ratios:")
    for i, ratio in enumerate(result_ratios):
        print(f"Pair {i+1}: ({sample_pairs[i][0]}, {sample_pairs[i][1]}) -> {ratio}")