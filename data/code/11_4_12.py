from math import gcd

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """Simplify a ratio of two integers by dividing both by their GCD."""
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both inputs must be integers.")
    
    common = gcd(abs(a), abs(b))
    simplified_a = a // common
    simplified_b = b // common
    
    # Ensure the sign convention: first non-zero element is positive.
    if (simplified_a < 0) or (simplified_a == 0 and simplified_b < 0):
        return -simplified_a, -simplified_b
        
    return simplified_a, simplified_b

def process_pairs(pairs_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Accept a list of length pairs and returns a list of their simplified ratios."""
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs_list):
        raise ValueError("All elements must be tuples of exactly two integers.")
    
    return [simplify_ratio(a, b) for a, b in pairs_list]

if __name__ == '__main__':
    sample_pairs = [(840, -56), (12, 3), (-9, 6), (7, 0)]
    
    # Process the input and get simplified ratios
    result_ratios = process_pairs(sample_pairs)
    
    print("Original pairs:", sample_pairs)
    print("Simplified ratios:", result_ratios)