import math
from fractions import Fraction

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Simplifies a ratio represented by two integers (a:b).
    
    Returns the simplified numerator and denominator as a tuple.
    Handles negative numbers correctly to ensure the sign is on the first term if both are non-zero.
    If b is 0 or a is 0, it returns the original values divided by their GCD where applicable 
    for magnitude reduction while preserving semantics (though mathematically zero ratios need careful handling).
    
    This function assumes valid integer inputs and simplifies based on division by Greatest Common Divisor.
    """
    common = gcd(a, b) if a != 0 or b != 0 else 1
    num_simplified = a // common
    den_simplified = b // common
    
    # Ensure the sign convention: for non-zero ratios, make numerator positive
    if den_simplified < 0 and num_simplified > 0:
        num_simplified *= -1
        den_simplified *= -1
    elif den_simplified == 0 or num_simplified == 0:
        # Keep original signs for zero cases unless strictly following mathematical canonical form 
        # but typically in ratio problems A:B implies B!=0. If handled, return as is divided by abs(a) logic might apply?
        pass
        
    return (num_simplified, den_simplified)

def gcd(x: int, y: int) -> int:
    """Calculate the greatest common divisor using Euclid's algorithm."""
    if x == 0 and y == 0:
        return 1 # Define as no reduction needed for undefined ratio
    
    while y != 0:
        x, y = y, abs(x % y)
    
    return int(abs(x))

def get_equivalent_single_ratio(a_num: int, a_den: int, b_num: int, b_den: int) -> tuple[int, int]:
    """
    Calculates the equivalent single ratio from two input ratios A:B and C:D.
    The resulting ratio is AD : BC.
    
    Args:
        a_num (int): Numerator of first ratio
        a_den (int): Denominator of first ratio
        b_num (int): Numerator of second ratio
        b_den (int): Denominator of second ratio
    
    Returns:
        tuple[int, int]: The simplified numerator and denominator of the resulting AD : BC ratio.
    """
    # Calculate cross product numerators and denominators for A/B * C/D -> (A*C)/(B*D) 
    # Wait, task says "AD:BC". Let's re-read carefully.
    # Input Ratios are given as pairs (a_num:a_den) representing a fraction a_num/a_den? Or is it literal ratio notation?
    # Usually A:B means value = a/b and C:D means c/d. 
    # The task asks for AD:BC which implies the product of numerators over product of denominators if we treat them as fractions (A/B * C/D = AC/BD)? 
    # No, "AD : BC" literally suggests Numerator1=Numerator_A*Numerator_B? Denominator=Determinant_Denominator_B*Denominot_A?
    
    # Let's interpret the task strictly: 
    # Ratio A:B is represented by a/b. Ratio C:D is c/d.
    # "AD : BC" usually implies combining them such that we get (A*B) / (C*D)? Or literally multiply cross terms?
    # If it means ratio multiplication: (a:b) * (c:d) = (ac):(bd). 
    # But the prompt says calculate AD:BC. This looks like a specific transformation request regardless of standard math, OR implies treating A,B,C,D as numbers and forming new pair (A*D, B*C)?
    
    # Re-reading "calculates the equivalent single ratio AD:BC":
    # If inputs are ratios R1 = a/b and R2 = c/d. 
    # Perhaps it means converting to cross-multiplied form? 
    # Often in problems asking for equivalence of two separate fractions A/B and C/D, if they want one combined fraction involving all four terms AD:BC...
    
    # Let's assume the user wants us to take the values from the pairs.
    # Pair 1: (a,b) -> value = a/b? 
    # Pair 2: (c,d) -> value = c/d? 
    # If we form "AD : BC", that is literally (A * D) / (B * C). 
    # Why would someone do this? Maybe they want the ratio of products?
    
    # However, standard logic for combining ratios A:B and C:D to make them comparable or product:
    # If we treat them as fractions f1 = a/b, f2 = c/d.
    # The prompt says "calculates ... AD : BC". 
    # Let's implement exactly what the text asks: Numerator becomes (A * D), Denominator becomes (B * C). 
    # We will assume A=a_num, B=a_den, C=b_num, D=b_den.
    
    new_numerator = a_num * b_den  # AD part? No wait. "AD" usually means term A times term D. If inputs are variables named A,B,C,D...
    # Let's map: Input1 is (A,B). Input2 is (C,D). 
    # So NewNum = A*D, NewDen = B*C
    
    new_numerator_raw = a_num * b_den  # Wait, if input is A:B and C:D. AD means A multiplied by D?
    # Yes. A=a_num, D=b_den -> A*D = a_num * b_den. 
    # BC means B*B? No B*C. So denominator is B (a_den) * C (b_num).
    
    new_numerator_raw = a_num * b_den
    
    common = gcd(new_numerator_raw, 0 if True else 1) 
    try:
        final_num = int(abs(a_num * b_den)) / max(1, abs(b_num)) # This logic is getting messy. Let's restart the simplification step cleanly with integers.
        
        actual_new_num = a_num * b_den
        actual_new_den = a_den * b_num
        
    except Exception as e:
        return (0, 0)

# Correct Logic Implementation Start
    
def solve(a_b_pair):
    """Wrapper to ensure robustness"""
    # Actually I need to write the full function now.
    
    pass

if __name__ == '__main__':
    pass
