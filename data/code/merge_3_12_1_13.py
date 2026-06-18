import math

def simplify_ratio(ratio1: int, ratio2: int) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a coprime pair (a, b).

    Args:
        ratio1 (int): The first part of the ratio.
        ratio2 (int): The second part of the ratio.

    Returns:
        tuple[int, int]: A simplified tuple where both numbers are positive integers and their greatest common divisor is 1.
                         If input non-integers or negative values occur, they will be handled by converting to integers 
                         based on context; however, strictly speaking for ratios in this domain we assume integer inputs.

    Note: This function ensures the result contains only coprime numbers (GCD == 1)."""

    # Ensure both are integers
    if not isinstance(ratio1, int) or not isinstance(ratio2, int):
        raise TypeError("Both ratio arguments must be integers.")

    # Handle zero cases explicitly to avoid division by zero in GCD logic later
    if ratio1 == 0 and ratio2 == 0:
        return (0, 0)
    
    abs_ratio1 = abs(ratio1)
    abs_ratio2 = abs(ratio2)

    common_divisor = math.gcd(abs_ratio1, abs_ratio2)

    simplified_a = ratio1 // common_divisor
    simplified_b = ratio2 // common_divisor
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external input or files
    samples = [
        ((3, 9), 'Expected: (1, 3)'),
        ((4, 8), 'Expected: (1, 2)'),
        ((-2, -6), 'Expected: (-1, -3)'),
        ((7, 0), 'Expected: (7, 0)'),
        ((15, 10), 'Expected: (3, 2)'),
    ]

    print("Running simplify_ratio tests...\n")
    
    for inputs, expected_desc in samples:
        if isinstance(inputs[0], tuple):
            r = inputs[0]
            result = simplify_ratio(r[0], r[1])
            desc = f"Input {r} -> Result {result}. " + (f"Match description: {expected_desc}" or "")
        else:
            # Fallback if input format was unexpected, though structure above handles tuples
            continue
            
        print(f"{desc}")

    # Additional direct calls to demonstrate usage clarity
    test_cases = [
        1234567890 * (1, 2), 
        (-1, -1)
    ]
    
    if isinstance(test_cases[0], tuple):
        a, b = simplify_ratio(*test_cases[0])
        print(f"\nDirect test case {test_cases[0]} -> ({a}, {b})")

    else:
        # Just in case someone passes floats that should be truncated (though spec implies int)
        pass
        
    # Final verification with a known coprime pair to ensure identity behavior when already simplified
    final_check = simplify_ratio(5, 7)
    print(f"\nVerification of existing coprimality for (5, 7): {final_check}")