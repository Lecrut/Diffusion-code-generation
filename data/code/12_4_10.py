import math
from fractions import Fraction

def simplify_ratios(weight_ratios):
    """
    Takes a list of weight ratios (as integers) and returns a new list 
    containing their simplified forms as tuples (numerator, denominator).
    
    A ratio is represented by two integers [a, b]. The function simplifies 
    the fraction a/b by dividing both numbers by their greatest common divisor.
    
    Args:
        weight_ratios (list of lists): List where each element is a list of two integers representing a ratio [numerator, denominator].
        
    Returns:
        list of tuples: A new list containing simplified ratios as immutable tuples.
    """
    if not isinstance(weight_ratios, list) or len(weight_ratios) == 0:
        return []

    result = []
    
    for ratio in weight_ratios:
        # Ensure the input is a pair of integers
        if not (isinstance(ratio, list) and len(ratio) == 2):
            raise ValueError(f"Each item must be a list of two integers. Got {ratio}")

        numerator = int(ratio[0])
        denominator = int(ratio[1])

        # Handle zero cases to avoid division by zero in logic, though math.gcd handles it gracefully for gcd(0,x)=x
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = math.gcd(numerator, abs(denominator))
        
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        
        result.append((simplified_numerator, simplified_denominator))

    return result

if __name__ == '__main__':
    # Hard-coded sample values representing weight ratios [numerator, denominator]
    samples = [
        [2, 4],      # Should simplify to (1, 2)
        [-3, 9],     # Should simplify to (-1, 3)
        [5, 7],      # Already simplified -> (5, 7)
        [0, 8],      # Simplifies to (0, 1)
        [4, -6]      # Simplifies to (-2, -3) or similar depending on sign convention; math.gcd handles absolute values for divisor
    ]

    simplified_results = simplify_ratios(samples)

    print("Original Ratios:", samples)
    print("Simplified Ratios:")
    
    for i, (original, simplified) in enumerate(zip(samples, simplified_results)):
        print(f"  {i}: {original} -> {simplified}")