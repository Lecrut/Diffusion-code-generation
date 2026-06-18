import math

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Returns a simplified ratio (a_num, b_num) such that 
    original = numerator * a / den and denom = denominator * b,
    where gcd(a_num, b_num) == 1.

    Handles large integers efficiently by using math.gcd which is implemented in C for Python's standard library.
    
    Args:
        numerator (int): The top value of the ratio.
        denominator (int): The bottom value of the ratio.
        
    Returns:
        tuple[int, int]: A simplified pair where the values are coprime and preserve the original ratio sign.

    Raises:
        ValueError: If both input integers are zero.
    """
    
    if numerator == 0 and denominator == 0:
        raise ValueError("Ratio cannot be formed with two zeros.")

    # Handle negative signs correctly (move negatives to numerator)
    has_negative = False
    sign_value = abs(numerator) * abs(denominator)
    
    actual_numerator = -numerator if num < 0 else numerator
    actual_denominator = denominator
    
    is_neg = (numerator < 0 and denominator > 0) or \
             (numerator > 0 and denominator < 0)

    # Ensure we always start with positive absolute values for GCD calculation, 
    # then apply the sign at the end to keep it consistent.
    
    a_num = abs(actual_numerator)
    b_num = abs(actual_denominator)
    
    common_divisor = math.gcd(a_num, b_num)
    
    simplified_a = a_num // common_divisor
    simplified_b = b_num // common_divisor
    
    # Apply sign back to the numerator if necessary (keep denominator positive for standard form)
    if is_neg:
        return -simplified_a, simplified_b
    else:
        return simplified_a, simplified_b

if __name__ == '__main__':
    # Hard-coded sample values representing potentially large integers
    n1 = 250_000_000_000
    d1 = -375_000_000_000
    
    a, b = simplify_ratio(n1, d1)
    
    print(f"Input: {n1} / {d1}")
    print(f"Simplified Ratio: {a} : {b}")