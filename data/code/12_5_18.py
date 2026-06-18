import math

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """Simplify a ratio (numerator/denominator) to its lowest terms."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor
    
    # Ensure the sign is consistent (positive denominator)
    if simplified_den < 0:
        simplified_num *= -1
        simplified_den *= -1
        
    return simplified_num, simplified_den

def multiply_ratios(ratio_a_b):
    """
    Takes two ratios A:B and C:D represented as tuples.
    Calculates the product ratio AD:BC and simplifies it.
    
    Args:
        ratio_a_b (tuple[int, int]): Represents A : B
    
    Returns:
        tuple[int, int]: The simplified product of the two ratios.
    """
    a, b = ratio_a_b[0], ratio_a_b[1]
    c, d = ratio_a_b[2], ratio_a_b[3]  # Assuming input is a single tuple with 4 values or we handle unpacking differently
    
    # If the function receives two separate tuples (A:B and C:D), this structure assumes 
    # they are passed in a way that allows accessing c and d.
    # To strictly follow "takes two ratios", let's adjust the logic to accept them as arguments 
    # or flatten if passed as one list of 4 ints, but based on typical usage:
    
    return simplify_ratio(a * d, b * c)

# Updated function signature for clarity accepting two tuples explicitly in main block logic
def combine_and_simplify_ratios(ratio1, ratio2):
    """
    Calculates the equivalent single ratio from two ratios (A:B and C:D).
    Returns AD:BC simplified.
    
    Args:
        ratio1 (tuple[int, int]): First ratio A : B
        ratio2 (tuple[int, int]): Second ratio C : D
    
    Returns:
        tuple[int, int]: Simplified result of the product.
    """
    a, b = ratio1[0], ratio1[1]
    c, d = ratio2[0], ratio2[1]
    
    # The cross-multiplication rule for ratios A/B * C/D gives (A*C)/(B*D) 
    # However, the task asks specifically to calculate AD:BC. 
    # Ratio multiplication of (A:B)*(C:D) is typically interpreted as fractions A/B * C/D = AC/BD.
    # But the prompt explicitly says "calculates the equivalent single ratio AD:BC".
    # This implies a specific transformation requested by the user, likely treating them differently 
    # or performing cross-multiplication in reverse order of denominators/numerators for some reason?
    
    # Re-reading carefully: "takes two ratios A:B and C:D ... calculates ... AD : BC"
    # If we treat them as fractions f1 = a/b, f2 = c/d. 
    # Standard multiplication is ac / bd.
    # The requested ratio is ad / bc. This equals (a * d) / (b * c).
    
    numerator_result = a * d
    denominator_result = b * c
    
    return simplify_ratio(numerator_result, denominator_result)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access.
    ratio1 = (2, 3)   # A:B
    ratio2 = (4, 5)   # C:D
    
    result_ratio = combine_and_simplify_ratios(ratio1, ratio2)
    
    print(f"Ratio {ratio1} : Ratio {ratio2}")
    print(f"Simplified Result AD:BC -> {result_ratio[0]}:{result_ratio[1]}")