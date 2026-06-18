import math

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """Simplify a ratio (a:b) to its lowest terms."""
    if b == 0:
        raise ValueError("Ratio denominator cannot be zero.")
    
    gcd = math.gcd(abs(a), abs(b))
    return a // gcd, b // gcd

def multiply_ratios(num1: int, den1: int, num2: int, den2: int) -> tuple[int, int]:
    """Calculate the product of two ratios (num1/den1 * num2/den2)."""
    if den1 == 0 or den2 == 0:
        raise ValueError("Denominator cannot be zero.")
    
    numerator = num1 * num2
    denominator = den1 * den2
    
    return simplify_ratio(numerator, denominator)

def calculate_combined_ratio(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """
    Takes two ratios A:B and C:D.
    Calculates the equivalent single ratio AD:BC (which represents 
    the product of the fractions A/B * C/D).
    
    Note: The prompt asks for "AD:BC". In standard mathematical terms involving 
    combining ratios multiplicatively, this corresponds to multiplying the numerators 
    and denominators respectively. If interpreted as a cross-multiplication result 
    from an equation like (A/B) = (C/D), that would imply A*D = B*C, not creating 
    a new ratio AD:BC. Given the instruction "calculates the equivalent single ratio",
    we interpret this as forming the fraction (A*B)/(B*A)? No, let's re-read carefully.
    
    Usually, when combining ratios in specific contexts (like compound interest or scaling),
    one might multiply them directly: (A/B) * (C/D). The result is (AC)/BD.
    
    However, the prompt explicitly says "calculates the equivalent single ratio AD:BC".
    This implies a direct construction of numerator = A*D and denominator = B*C? 
    Or does it mean the cross product used in proportion checks?
    
    Let's look at the phrasing again: "takes two ratios A:B and C:D, and calculates 
    the equivalent single ratio AD:BC".
    
    If I have Ratio1 = 2:3 (value 0.66) and Ratio2 = 4:5 (value 0.8).
    Product value = 0.528.
    AC/BD = 8/15 = 0.533... Close but not exact due to rounding in my head. 
    Actually 2*4 / 3*5 = 8/15 = 0.533.
    
    AD/BC would be (2*5) / (3*4) = 10/12 = 5/6 = 0.833... This is not the product of values.
    
    Perhaps it refers to finding a ratio X:Y such that A:B :: C:D implies something? 
    No, "equivalent single ratio AD:BC" sounds like an instruction to construct 
    the pair (A*D) : (B*C). Why would one do that? It's often used in solving proportions 
    where you cross multiply.
    
    Let's assume the task literally means constructing a new numerator from A and D, 
    and a new denominator from B and C. i.e., Result = (A * D) : (B * C).
    Then simplify it."""
    
    # Construct AD:BC as requested by the literal text "AD:BC"
    num_result = a * d
    den_result = b * c
    
    return multiply_ratios(num_result, den_result)

if __name__ == '__main__':
    # Sample values for testing
    ratio_a_b_num = 2
    ratio_a_b_den = 3
    ratio_c_d_num = 4
    ratio_c_d_den = 5
    
    result_num, result_den = calculate_combined_ratio(
        ratio_a_b_num, 
        ratio_a_b_den, 
        ratio_c_d_num, 
        ratio_c_d_den
    )
    
    print(f"Input Ratios: {ratio_a_b_num}:{ratio_a_b_den} and {ratio_c_d_num}:{ratio_c_d_den}")
    print(f"Calculated Combined Ratio (AD:BC): {result_num}:{result_den}")