def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two integers l1:l2 using the Euclidean algorithm.
    
    Args:
        l1 (int): The first length value.
        l2 (int): The second length value.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator 
                         of the simplified ratio as integers.
                         
    Raises:
        ValueError: If either input is zero or if inputs are not positive integers.
    """
    
    # Validate inputs to ensure they form a valid non-zero ratio
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Lengths must be positive integers.")

    def euclidean_gcd(a: int, b: int) -> int:
        """Helper function using the Euclidean algorithm to find GCD."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

    # Calculate Greatest Common Divisor (GCD) of l1 and l2
    common_divisor = euclidean_gcd(l1, l2)

    # Simplify the ratio by dividing both numbers by their GCD
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor

    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        (40, 60),   # Expected: (2, 3)
        (75, 150),  # Expected: (1, 2)
        (8, 12),    # Expected: (2, 3)
        (9, 9),     # Expected: (1, 1)
        (100, 25),  # Expected: (4, 1)
    ]

    print("Ratio Calculation Results:")
    for l in test_cases:
        ratio = find_ratio_of_lengths(*l)
        original_str = f"{l[0]}:{l[1]}"
        simplified_str = f"{ratio[0]}:{ratio[1]}"
        print(f"Original {original_str} -> Simplified {simplified_str}")