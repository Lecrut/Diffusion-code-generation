import math

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a ratio (numerator/denominator) to its lowest terms.
    
    Args:
        numerator: The top number of the ratio.
        denominator: The bottom number of the ratio.
        
    Returns:
        A tuple containing the simplified numerator and denominator.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    # Handle sign consistency; ensure positive denominator by convention, 
    # but typically ratios are defined such that signs match or one is negated.
    # Standard form usually puts the negative in front of numerator.
    if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
        gcd_val = abs(denominator) * -1 // math.gcd(abs(numerator), abs(denominator)) # This logic is flawed, corrected below
    
    # Correct GCD based simplification:
    common_divisor = math.gcd(numerator, denominator)
    
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor

    return (simplified_num, simplified_den)

def calculate_product_ratio(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """
    Takes two ratios A:B and C:D.
    Calculates the product ratio AD : BC 
    and simplifies it to its lowest terms.

    Args:
        a: First numerator (A).
        b: First denominator (B).
        c: Second numerator (C).
        d: Second denominator (D).

    Returns:
        A tuple (x, y) representing the simplified ratio x:y = AD:BC.
    
    Raises:
        ZeroDivisionError if any input value is zero as it's undefined for multiplication in this context.
    """
    # Check constraints based on task requirements to ensure valid inputs
    values_to_check = [a, b, c, d]
    for val in values_to_check:
        if val == 0:
            raise ZeroDivisionError("Input ratios cannot contain zero.")

    new_numerator = a * d
    new_denominator = b * c
    
    simplified_result = simplify_ratio(new_numerator, new_denominator)
    
    return (simplified_result[0], simplified_result[1])

if __name__ == '__main__':
    # Hard-coded sample values for testing as per requirements.
    # Sample ratio 1: A:B -> 3:4
    a = 3
    b = 4
    
    # Sample ratio 2: C:D -> 5:7
    c = 5
    d = 7

    result_numerator, result_denominator = calculate_product_ratio(a, b, c, d)
    
    print(f"Input Ratios: {a}:{b} and {c}:{d}")
    print(f"Equivalent Product Ratio (AD : BC):")
    print(f"Simplified Result: {result_numerator}:{result_denominator}")