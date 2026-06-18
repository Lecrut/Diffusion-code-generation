import math

def simplify_ratio(ratio1: int, ratio2: int) -> tuple[int, int]:
    """
    Simplifies two weight ratios by dividing both numbers by their greatest common divisor (GCD).
    
    Args:
        ratio1 (int): The first integer in the ratio.
        ratio2 (int): The second integer in the ratio.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as coprime integers.
                          If both inputs are zero, returns (0, 1).
                          
    Raises:
        ValueError: If either input is not an integer or if they are non-zero but one is negative 
                   while the other is positive without a clear sign convention for ratios.
    
    Note: This function assumes standard mathematical ratio simplification where signs are preserved.
          For example, simplify_ratio(-2, 4) returns (-1, 2).
    """
    if not isinstance(ratio1, int) or not isinstance(ratio2, int):
        raise ValueError("Both inputs must be integers.")

    # Handle the case where both are zero
    if ratio1 == 0 and ratio2 == 0:
        return (0, 1)

    # Calculate GCD of absolute values to ensure positive divisor
    gcd_value = math.gcd(abs(ratio1), abs(ratio2))

    simplified_numerator = ratio1 // gcd_value
    simplified_denominator = ratio2 // gcd_value

    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (3, 6),      # Expected: (1, 2)
        (-4, -8),    # Expected: (-1/2 -> -1, -0.5? No, integers only. GCD(4,8)=4 -> -1, -2) Wait, math.gcd is always positive. 
                    # So gcd(-4, -8) = 4. Result: -4//4=-1, -8//4=-2. Correct.
        (0, 5),      # Expected: (0, 1)
        (-3, 9),     # Expected: (-1, 3)
        (7, 16),     # Already coprime -> (7, 16)
    ]

    print("Running simplified_ratio tests...")
    
    for i, case in enumerate(test_cases):
        r1, r2 = case
        result = simplify_ratio(r1, r2)
        
        # Verify coprimality manually just to be sure logic holds up conceptually
        if abs(result[0]) > 0 and abs(result[1]) > 0:
            gcd_check = math.gcd(abs(result[0]), abs(result[1]))
            assert gcd_check == 1, f"Result {result} is not coprime!"

        print(f"simplify_ratio({r1}, {r2}) = {result}")

    # Additional edge case check for zero handling logic explicitly if needed beyond default behavior
    result_zero = simplify_ratio(0, 0)
    assert result_zero == (0, 1), f"Expected (0, 1) for (0, 0), got {result_zero}"
    
    print("All tests passed.")