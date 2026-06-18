import math

def simplify_ratio(ratio_list):
    """
    Takes a list of weight ratios (as lists/tuples) and returns a new list 
    containing simplified forms where each element is represented as [numerator, denominator].
    
    A ratio [a, b] is simplified by dividing both elements by their greatest common divisor.
    Negative numbers are handled to ensure the sign appears only in the numerator if necessary.
    Zero denominators are not allowed; if present, they raise a ValueError.

    Args:
        ratio_list (list of list/tuple): List of weight ratios. Each inner element should be 
                                        representable as two numbers [numerator, denominator].

    Returns:
        list of tuple: Simplified ratios represented as tuples [(n1, d1), (n2, d2), ...]

    Raises:
        ValueError: If any ratio has a zero denominator.
    
    Example usage:
        >>> simplify_ratio([[4, 6], [7, -35]])
        [(2, 3), (-1, 5)]
    """
    simplified = []
    for r in ratio_list:
        if not isinstance(r, (list, tuple)):
            raise TypeError(f"Each element must be a list or tuple of two numbers. Got {type(r)}")
        
        num = float(r[0])
        den = float(r[1])

        # Check for zero denominator
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        gcd_val = math.gcd(int(abs(num)), int(abs(den)))
        simplified_num = int(num / gcd_val)
        simplified_den = int(den / gcd_val)

        # Ensure canonical form: positive denominator, negative numerator if needed
        if simplified_den < 0:
            simplified_num = -simplified_num
            simplified_den = -simplified_den
        
        simplified.append((int(simplified_num), int(simplified_den)))

    return simplified

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_ratios = [
        [4, 6],      # Should simplify to (2, 3)
        [-8, -12],   # Should simplify to (-2, -3) -> canonicalized to (-2, -3)? Wait: gcd logic applies absolute values. 
                    # GCD(8,12)=4 => num=-2, den=-3 => flip signs => (-(-2), -( -3))? No wait...
                    # Let's re-evaluate manually for [-8, -12]:
                    # abs(num)=8, abs(den)=12 -> gcd=4
                    # simplified_num = -8/4 = -2
                    # simplified_den = -12/4 = -3
                    # Since den < 0: num becomes +2, den becomes +3? Wait no.
                    # The rule is usually keep sign in numerator if denominator negative -> flip both signs to make denom positive.
                    # So [-8,-12] -> gcd=4 -> (-2, -3) -> flip => (2, 3). 
                    # But wait, mathematically -8/-12 = 2/3. Correct result should be (2, 3).
        [7, -35],    # Should simplify to (1, -5) -> canonicalized to (-1, 5)? No: 7/-35 = -0.2 => -1/5. 
                    # GCD(7,35)=7 -> num=1, den=-5 -> flip signs => (-1, 5).
        [0, 5],      # Should simplify to (0, 1)
        [-6, 9]      # Should simplify to (-2, 3)
    ]

    result = simplify_ratio(test_ratios)
    
    print("Input Ratios:", test_ratios)
    print("Simplified Ratios:", result)