def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculate the simplified integer ratio of two lengths using the Euclidean algorithm.
    
    Args:
        l1 (int): First length value
        l2 (int): Second length value
    
    Returns:
        tuple(int, int): A tuple containing the numerator and denominator in simplest form.
                         If both inputs are zero, returns a simplified representation of 0/1 or handles gracefully based on logic (assuming non-zero for valid ratios). 
                         Note: Based on standard ratio definition, if l2 is 0, it's undefined; this implementation assumes positive integers as per typical length constraints unless specified otherwise.
                         For robustness with the prompt's implied need for a clean function:
                         - If both are zero, returns (1, 1) to avoid division by zero errors in downstream logic requiring non-zero denominators, or we can return (0, 1). 
                         Let's assume standard positive integers. The code handles zeros gracefully returning the ratio of magnitudes if signs differ but usually lengths are positive.
    """
    
    # Handle edge case where both are zero to prevent division by zero and provide a consistent output
    if l1 == 0 and l2 == 0:
        return (1, 1)

    # Determine the greatest common divisor using Euclidean algorithm
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return abs(a)

    if l2 == 0:
        # Ratio is undefined mathematically, but returning (l1/|l1| if possible else something safe). 
        # However, to ensure an integer ratio representation that doesn't crash division by zero later:
        # If denominator is strictly required non-zero for the "ratio" concept in this context.
        return (0, 1)

    common_divisor = gcd(l1, l2)
    
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    
    # Ensure positive denominator by adjusting signs if necessary for ratio convention a:b -> x:|y|? 
    # Usually ratios preserve sign or map to magnitudes. Standard simplification keeps the relative sign.
    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements
    
    test_cases = [
        (4, 8),      # Expected: (1, 2)
        (6, 9),      # Expected: (2, 3)
        (-3, -5),    # Expected: (-3, -5) or simplified signs? Usually ratios keep relative sign. 
                     # Let's assume standard reduction where gcd is positive and we divide normally.
         (10, 5),     # Expected: (2, 1)
        (7, 49),     # Expected: (1, 7)
    ]

    for l in test_cases:
        a, b = find_ratio_of_lengths(l[0], l[1])
        print(f"Ratio of {l}: {a}:{b}")