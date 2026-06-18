import math

def simplify_ratio(ratio1: tuple | list) -> float:
    """
    Calculate and return the simplified ratio of two input weight ratios.
    
    The function takes two lists or tuples representing (component1, component2),
    computes their individual GCDs to normalize each pair separately by dividing 
    both components by their greatest common divisor, then returns the resulting 
    normalized first value divided by the second.

    Args:
        ratio1 (tuple | list): First weight ratio as a sequence of two numbers.

    Returns:
        float: The simplified ratio in lowest terms.
    
    Raises:
        ValueError: If input sequences do not contain exactly two numeric elements or are empty/non-numeric.
    """
    
    def normalize_pair(pair) -> tuple[float, ...]:
        if not isinstance(pair, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        
        if len(pair) != 2:
            raise ValueError(f"Expected a pair of two numbers, got {len(pair)}.")
            
        for item in pair:
            if not isinstance(item, int):
                raise TypeError(f"All elements in the ratio must be integers. Got {type(item).__name__}.")

        gcd_val = math.gcd(int(pair[0]), int(pair[1]))
        
        return (int(pair[0]) // gcd_val, int(pair[1]) // gcd_val)
    
    normalized_pair1 = normalize_pair(ratio1)
    simplified_ratio = float(normalized_pair1[0] / normalized_pair1[1])
    
    return simplified_ratio

if __name__ == '__main__':
    sample_ratios = [(3, 9), (2, 4)]
    result_ratio = simplify_ratio(sample_ratios[0])