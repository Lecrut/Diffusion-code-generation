import math

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Calculates the ratio of two integers a/b in its simplest form.
    
    The function computes the greatest common divisor (GCD) of |a| and |b|,
    then divides both numbers by this GCD to return them as a tuple.

    Args:
        a (int): The numerator integer. Can be large or negative.
        b (int): The denominator integer. Must not be zero for valid mathematical ratio logic 
                 within the context of simplification, though division by zero will raise an error naturally in Python 3 if attempted via float conversion later; here we return simplified integers.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.

    Raises:
        ZeroDivisionError: If b is zero (division by zero conceptually invalid for ratio).
    
    Note:
        The function handles large integers efficiently using Python's arbitrary precision arithmetic 
        and the built-in math.gcd which supports large inputs robustly.
    """
    if b == 0:
        raise ZeroDivisionError("Ratio denominator cannot be zero.")

    # Use absolute values for GCD calculation to handle negative numbers correctly,
    # but preserve signs in the final result relative to input a and b.
    gcd_value = math.gcd(abs(a), abs(b))
    
    simplified_numerator = a // gcd_value
    simplified_denominator = b // gcd_value
    
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [
        (100, 25),      # Expected: (4, 1)
        (-8, -4),       # Expected: (-2, -1) -> simplified to same sign logic usually keeps signs consistent with inputs unless normalized; here we keep input sign distribution divided by GCD. 
                       # Standard simplification often normalizes so denominator is positive if possible, but task says "dividing both", implying direct division.
        (750000000000000000000000, 3),   # Large integer test case to verify robustness with big ints. Expected: (...large num simplified by 1... wait GCD of large and 3) -> depends on divisibility
        (6, -9),        # Mixed signs expected (-2/-3 or similar depending on strict interpretation). Direct division yields (-2, -3). 
                       # Often ratios are presented with positive denominator. Let's stick to the literal instruction: "dividing both by their GCD".
    ]

    for num, den in test_cases:
        try:
            simplified = simplify_ratio(num, den)
            print(f"Ratio of {num} / {den}:")
            print(f"Simplified Numerator ({simplified[0]}), Denominator ({simplified[1]})")
            
            # Optional verification logic to ensure correctness for display purposes (not part of return spec but good sanity check in main)
            if den != 0:
                original_ratio = num / den
                simplified_float_val = simplified[0] / simplified[1]
                
                assert abs(original_ratio - simplified_float_val) < 1e-9, "Simplified ratio does not match original."
        except ZeroDivisionError as e:
            print(f"Error for {num} / {den}: {e}")