import math
from fractions import Fraction

def simplify_ratio_pair(pair):
    """Simplify a pair of numbers into their lowest terms ratio as a tuple (numerator, denominator)."""
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a list or tuple with exactly two elements.")

    try:
        num = float(pair[0])
        den = float(pair[1])
    except (ValueError, TypeError):
        raise ValueError(f"Both elements in the pair must be numbers. Got {pair}")

    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    # Handle negative signs correctly to keep denominator positive where possible, or follow standard fraction sign rules
    # Standard Fraction handles this well by keeping numerator and denominator integers with minimal gcd
    try:
        frac = Fraction(int(num), int(den))
    except (ValueError, OverflowError):
        raise ValueError("Inputs must be representable as exact fractions.")

    return (frac.numerator, frac.denominator)

def process_ratio_list(pairs):
    """Accept a list of length pairs and returns a list of simplified ratios."""
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    result = []
    for pair in pairs:
        ratio = simplify_ratio_pair(pair)
        # Ensure we don't include 0/1 or similar trivial cases if desired, but keeping all simplifications here.
        result.append(ratio)
    
    return result

if __name__ == '__main__':
    sample_pairs = [
        (4, 8),   # Should simplify to (1, 2)
        (-3, -9), # Should simplify to (-1, -3) or similar depending on fraction logic; Fraction(-3,-9)->-3/9 -> -1/-3? Actually Fraction keeps sign in numerator usually. Let's test mentally: Fraction(-3, -9) is 0.33 which is 1/3 but signs cancel out to positive denominator by default behavior of fractions module if we don't force negative denom. 
                  # Python'sFraction constructor does not guarantee a specific form for negatives unless simplified manually.
                  # Actually: Fraction(-3, -9) -> gcd(3,9)=3 -> (-1)/(-3). Python keeps signs such that denominator is positive? No, standard fraction logic in float->int conversion might vary slightly but let's rely on fractions module directly which does its own canonicalization mostly keeping denominator > 0 if possible or just reducing magnitude.
                  # Correction: Fraction(int(a), int(b)) ensures minimal integers with gcd reduced. 
        (10, -20),# Should simplify to (-3/6)? No -> 1/-2 = -1/2? Actually Fraction(10,-20) is 1/-2 which reduces to -1/2 internally by making denominator positive?
                  # Let's trace: gcd(10, 20)=10. Signs cancel for value but representation? 
        (5,),     # Invalid length, should raise error if called on this alone, but list is valid structure here.
    ]

    # Corrected sample with proper pairs only to avoid runtime crashes during testing phase without explicit input handling logic being triggered by bad indices in loop.
    
    test_data = [
        (4, 8),
        (-6, -12), 
        (7, 105),
        (3, -9)
    ]

    try:
        simplified_ratios = process_ratio_list(test_data)
        
        print("Original Pairs:")
        for p in test_data:
            print(f"({p[0]}, {p[1]})")
            
        print("\nSimplified Ratios (numerator, denominator):")
        for orig, simplified in zip(test_data, simplified_ratios):
            print(f"{orig} -> ({simplified[0]}, {simplified[1]})")

    except Exception as e:
        print(f"Error processing ratios: {e}")