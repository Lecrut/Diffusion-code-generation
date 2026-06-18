def find_ratio_of_lengths(l1, l2):
    """
    Calculates the simplified integer ratio of two lengths l1:l2 using 
    the Euclidean algorithm to compute their Greatest Common Divisor (GCD).
    
    Args:
        l1 (int or float): First length value.
        l2 (int or float): Second length value.
        
    Returns:
        tuple[int, int]: A tuple containing two integers representing 
                         the simplified ratio numerator and denominator.
                         
    Raises:
        ValueError: If either input is zero.
    """
    
    def gcd(a, b):
        # Euclidean algorithm to compute GCD
        while b != 0:
            a, b = b, a % b
        return abs(a)

    if l1 == 0 or l2 == 0:
        raise ValueError("Lengths cannot be zero.")

    # Ensure inputs are effectively integers for ratio representation.
    # If floats have negligible difference from their integer part, cast them.
    try:
        num = int(round(float(l1)))
        den = int(round(float(l2)))
        
        if num == 0 or den == 0:
            raise ValueError("Lengths cannot be zero.")

        common_divisor = gcd(num, den)
        
        return (num // common_divisor, den // common_divisor)
    except Exception as e:
        # Fallback for unexpected types if rounding fails unexpectedly 
        # by attempting direct int conversion first.
        try:
            num = int(l1)
            den = int(l2)
            
            if num == 0 or den == 0:
                raise ValueError("Lengths cannot be zero.")

            common_divisor = gcd(num, den)
            
            return (num // common_divisor, den // common_divisor)
        except Exception as e2:
            # Final fallback handling specific edge cases if needed 
            # though standard int/float logic should cover valid math inputs.
            raise ValueError(f"Invalid input types or values for ratio calculation.") from None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    test_cases = [
        (10, 5),      # Expected: (2, 1)
        (36, 48),     # Expected: (3, 4)
        (7.5, 2.5),   # Expected: (3, 1) - floats reduced to integers first
        (0, 5),       # Should raise ValueError
    ]

    for l1_val, l2_val in test_cases:
        try:
            result = find_ratio_of_lengths(l1_val, l2_val)
            print(f"Input ({l1_val}, {l2_val}) -> Ratio: {result[0]}:{result[1]}")
        except ValueError as ve:
            print(f"Error for input ({l1_val}, {l2_val}): {ve}")

    # Specific test with floats to ensure rounding logic works correctly
    float_test = find_ratio_of_lengths(7.5, 2.5)
    assert float_test == (3, 1), f"Float ratio failed: expected (3, 1), got {float_test}"
    print("Float ratio verification passed.")