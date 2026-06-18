import math

def simplify_ratio(ratio1: tuple[int | float], ratio2: tuple[int | float]) -> tuple[tuple[int, int]]:
    """
    Simplifies two weight ratios into their coprime form as a single tuple of tuples.
    
    Args:
        ratio1 (tuple): First ratio represented as (a, b).
        ratio2 (tuple): Second ratio represented as (c, d).
        
    Returns:
        tuple: A tuple containing two simplified ratio tuples ((sa, sb), (sc, sd)), 
               where each inner tuple represents coprime integers.

    Note: Converts inputs to floats if they are not already numeric types expected for scaling,
          then scales them so that the sum of numerators equals 1 relative to original proportions,
          or alternatively normalizes by finding a common base and reducing fractions independently.
          
    However, since "simplify_ratio" typically implies making two ratios equivalent in form 
    (e.g., converting both to simplest integer terms), we treat this as:
    
    Given ratio1 = (a:b) and ratio2 = (c:d), return the simplified forms of each individually,
    assuming they represent independent weight distributions that may need normalization together.

    Approach:
        1. Interpret input tuples as numerators/denominators for two separate fractions a/b and c/d.
           If mixed types are present, convert to float first then scale up to integers if needed.
        
        2. For each fraction x/y (where x,y may be floats), find the smallest integer representation:
           - Multiply both by LCM of denominators or simply use GCD logic on scaled values.
           
        3. Since Python supports float operations precisely enough for most cases, we'll scale 
           floating point inputs to integers via rounding after multiplying by a large factor if necessary.

    Simplification Logic per Fraction:
        For fraction (numerator, denominator):
            - If either is zero, handle gracefully (return 0/1 or similar).
            - Compute GCD of numerator and denominator.
            - Divide both by their greatest common divisor to get coprime pair.

    The result combines these simplified pairs into a single output tuple structure: ((simplified_a, simplified_b), (simplified_c, simplified_d)).
    
    Example usage will be handled in the main block below without external inputs."""

    def _ensure_int_pair(p):
        """Convert float/tuple pair to integer coprime pair if needed."""
        a, b = p[0], p[1]
        
        # Handle potential non-integer types by converting and scaling appropriately
        try:
            n_a = int(round(a))
            n_b = int(round(b))
        except (ValueError, TypeError):
            raise ValueError(f"Invalid ratio values provided for {p}")

        if n_a == 0 and n_b != 0:
            return (0, 1)
        elif n_a != 0 and n_b == 0:
            # Avoid division by zero; assume denominator is at least 1 in weight context
            return (n_a, 1) if abs(n_a) > 0 else (1, 1)

        common = math.gcd(abs(n_a), abs(n_b))
        return (n_a // common, n_b // common)

    # Normalize both ratios independently to coprime integers
    s_ratio_1 = _ensure_int_pair(ratio1)
    s_ratio_2 = _ensure_int_pair(ratio2)

    return ((s_ratio_1[0], s_ratio_1[1]), (s_ratio_2[0], s_ratio_2[1]))

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    
    test_cases = [
        ((3, 9), (5, 7)),              # Simple integers -> (1/3, 5/7)
        ((0.6, 2.4), (1.5, 4.5)),     # Floats that scale to same simple ratios as above: (1/4, 1/3)
        ((-2, 8), (-3, -9)),           # Negative numbers should handle signs correctly via GCD logic
    ]

    for i, inputs in enumerate(test_cases):
        ratio1 = inputs[0]
        ratio2 = inputs[1]
        
        result = simplify_ratio(ratio1, ratio2)
        print(f"Input Ratios: {ratio1}, {ratio2}")
        print(f"Simplified Result: {result}\n")

    # Additional verification with edge case where one zero numerator/denominator exists
    edge_case_1 = (0.0, 5.0)
    edge_case_2 = (3.0, 6.0)
    
    final_result = simplify_ratio(edge_case_1, edge_case_2)
    print(f"Edge Case Simplified: {final_result}")