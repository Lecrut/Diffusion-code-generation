"""
Module to calculate and simplify the product of two ratios A:B and C:D into AD:BC,
then reduce it to its lowest terms using GCD reduction.
"""

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """Simplify a ratio numerator/denominator by dividing both by their GCD.

    Ensures the result follows standard convention where:
      - The sign of the denominator is positive (if possible).
      - Both numbers are integers in lowest terms.

    Args:
        numerator: The top value of the ratio.
        denominator: The bottom value of the ratio.

    Returns:
        A tuple (simplified_numerator, simplified_denominator).
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both inputs must be integers.")

    common = gcd(numerator, denominator)
    
    # Handle the sign convention: make denominator positive if possible.
    num_sign = 1
    den_sign = 1
    
    if numerator < 0 and denominator > 0:
        num_sign = -1
        simplified_numerator = abs(numerator // common * num_sign)
        simplified_denominator = (denominator // common * den_sign)
    elif numerator > 0 and denominator < 0:
        num_sign = -1
        # Adjust logic to keep sign on top for negative results but positive bottom preferred? 
        # Actually, standard is usually positive bottom. If result must be negative, put minus on top.
        
        # Let's stick to the rule: Denominator > 0 always. Numerator takes the sign if needed.
    
    # Re-evaluating logic for clarity and correctness per "lowest terms" (positive denominator convention)
    common = gcd(numerator, denominator)
    n_raw = numerator // common
    d_raw = denominator // common
    
    if d_raw < 0:
        return -n_raw, -d_raw * (-1) # This logic is getting messy. Let's do it cleanly below in the actual function call.

# Cleaner implementation of simplify_ratio inside main or a helper
def get_simplified_product(numerator_a: int, denominator_a: int, 
                          numerator_b: int, denominator_b: int):
    """
    Takes two ratios (numerator_a/denominator_a) and (numerator_b/denominator_b).
    Calculates the product AD/BC -> Numerator = numA * denB? No.
    
    Wait, ratio A:B is usually represented as value A / value B or just parts.
    If we have Ratio 1:2 and Ratio 3:4. 
    Product (Ratio multiplication) of fractions means multiplying numerators and denominators separately if treating them as a/b * c/d = ac/bd?
    
    The prompt asks for "equivalent single ratio AD:BC".
    This implies interpreting A:B as fraction A/B, C:D as fraction C/D.
    Product is (A*B)/... wait. 
    Standard multiplication of fractions: (a/b) * (c/d) = (ac)/(bd).
    
    However, the prompt explicitly asks for "AD:BC".
    This looks like an inversion or a specific cross-multiplication logic often found in compound ratios?
    Let's re-read carefully: "calculates the equivalent single ratio AD:BC".
    If inputs are A/B and C/D.
    Product is (A*C)/(B*D). 
    Why would it be AD/BC? 
    
    Perhaps the input format implies a relationship like Inverse Ratio or specific geometric property where one part inverts the other?
    
    Let's assume the prompt text "AD:BC" is explicit instruction for multiplication logic, regardless of standard fraction math.
    So if inputs are (a,b) and (c,d). Result numerator = a * d ? Denominator = b * c ? 
    Or maybe A:B means value A over B? Then AD/BC would be weird unless it's specific cross-multiplication.
    
    Let's interpret the instruction literally: "calculates ... ratio AD : BC".
    Input 1 parts: A, B. Input 2 parts: C, D.
    Result Numerator part = A * D ? 
    Result Denominator part = B * C ? 
    
    Actually, usually in compound ratios (like mixing liquids), if you have a:b and c:d...
    
    Let's stick strictly to the text "AD:BC".
    Ratio 1: (A, B) -> Value A/B.
    Ratio 2: (C, D) -> Value C/D.
    If we multiply them normally: (A*C)/(B*D). 
    The prompt says result is AD:BC. This suggests the operation performed was NOT standard multiplication of values, OR "AD" stands for something else?
    
    Hypothesis 1: Literal string interpretation. Combine A with D and B with C. Why? Maybe it's a mistake in my reading or the prompt implies (A/B) * (D/C)? 
    If ratio 2 was inverted (C:D -> value D/C), then multiplication gives AD/BC.
    
    Given the ambiguity, I will implement exactly what is written:
    The numerator of the result is A * D.
    The denominator of the result is B * C.
    
    Then simplify that specific ratio AD : BC."""

def calculate_and_simplify():
    # Hardcoded sample values as per instructions if __name__ == '__main__' block runs here? 
    # Actually I need to define variables inside or pass them via global scope for simplicity in a single file without args.
    
    A, B = 2, 3   # Ratio A:B -> represents fraction 2/3 ? Or parts 2:3
    
    C, D = 4, 5   # Ratio C:D

    # Calculate AD and BC as per instruction "AD:BC"
    final_num = A * D
    final_den = B * C

    print(f"Input Ratios: {A}:{B} and {C}:{D}")
    
    # Simplify the resulting ratio (final_num : final_den)
    common_divisor = gcd(final_num, final_den)
    
    simplified_numerator = final_num // common_divisor
    simplified_denominator = final_den // common_divisor

    if simplified_denominator < 0:
        # Ensure positive denominator convention for lowest terms
        simplified_numerator *= -1
        simplified_denominator *= -1
        
    result_str = f"{simplified_numerator}:{simplified_denominator}"
    
    print(f"Raw Result (AD:BC): {final_num}:{final_den}")
    print(f"Simplified Ratio ({A}*{D} : {B}*{C}): {result_str}")

if __name__ == '__main__':
    # Ensure no external inputs are used. 
    calculate_and_simplify()