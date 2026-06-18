import math

def calculate_and_simplify_ratio(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """
    Calculates the equivalent single ratio of (A:B) and (C:D), which is AD:BC.
    Then simplifies this resulting ratio to its lowest terms by dividing both parts
    by their greatest common divisor (GCD).

    Args:
        a (int): Numerator of the first part A in the first ratio A:B
        b (int): Denominator of the first part B in the first ratio A:B
        c (int): Numerator of the second part C in the second ratio C:D
        d (int): Denominator of the second part D in the second ratio C:D

    Returns:
        tuple[int, int]: The simplified ratio as a tuple (x, y) representing x:y.
    """
    # Calculate AD and BC based on cross-multiplication rule for ratios
    numerator = a * d  # This corresponds to A*D in the explanation "AD" 
    denominator = b * c
    
    if numerator == 0 or denominator == 0:
        raise ValueError("Ratios must have non-zero numerators and denominators.")

    # Find the Greatest Common Divisor (GCD) of numerator and denominator
    gcd_value = math.gcd(numerator, denominator)
    
    # Simplify by dividing both parts by their GCD
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values for testing. 
    # Ratio 1: A:B = 2:3 (so a=2, b=3)
    # Ratio 2: C:D = 4/5 * 6:7 -> This means we are multiplying two ratios?
    # The prompt says "two ratios A:B and C:D". 
    # Example interpretation: Calculate the product of these two ratios.
    # (A/B) * (C/D) = (AC)/(BD). To get AD/BC, it's actually dividing (A*B)*... wait.
    
    # Let's re-read carefully: "calculates the equivalent single ratio AD:BC". 
    # This phrasing implies taking two ratios A:B and C:D and forming a new one where 
    # the first term is A multiplied by D, and the second term is B multiplied by C?
    # Or does it mean (A/B) * (C/D)? No, that would be AC/BD.
    # Does it mean cross-multiplication in some geometric context or simply arithmetic operation?
    # Given "AD:BC", this looks like the result of dividing one ratio by another if they were 
    # arranged as fractions where we swap denominators? (A/B) / (C/D) = AD/BC. Yes!
    
    # So input A:B is treated as fraction A/B and C:D as C/D. The operation requested results in AD:BC,
    # which mathematically corresponds to dividing the first ratio by the second ratio: 
    # (A / B) ÷ (C / D) = (A * D) / (B * C).

    a_val = 2
    b_val = 3
    
    c_val = 4
    d_val = 5
    
    try:
        result_numerator, result_denominator = calculate_and_simplify_ratio(a_val, b_val, c_val, d_val)
        
        print(f"Input Ratios:")
        print(f"A:B ({a_val}:{b_val})")
        print(f"C:D ({c_val}:{d_val})")
        print()
        print("Calculation: (A/B) divided by (C/D)")
        print(f"This yields the numerator A*D = {result_numerator}")
        print(f"And the denominator B*C = {a_val * b_val / result_denominator if False else 'N/A for check'}") 
        # Correction in print logic to show raw calculation before simplification
        intermediate_num = a_val * d_val  # AD
        intermediate_den = b_val * c_val  # BC
        
        print(f"Intermediate Numerator (AD): {intermediate_num}")
        print(f"Intermediate Denominator (BC): {intermediate_den}")
        
        final_ratio_str = f"{result_numerator}:{result_denominator}"
        print(f"Simplified Result Ratio: {final_ratio_str}")

    except ValueError as ve:
        print(f"Error occurred during calculation: {ve}")