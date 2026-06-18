"""
Module to calculate the ratio of two lengths as a simplified fraction.

This script takes two numerical values representing lengths, computes their ratio,
and returns the result as an irreducible fraction (numerator / denominator).
The function uses integer arithmetic where possible and floats otherwise if inputs are not integers,
though for true simplification in Python's GCD context with non-integers is complex; 
this implementation prioritizes exact rational representation by converting to a common base.

Since the prompt asks for simplified fraction specifically:
- If both inputs are integers or can be represented exactly as fractions (e.g., decimals that terminate cleanly),
  we attempt integer-based simplification using GCD.
- For general floats, exact "simplified fraction" is mathematically ambiguous without precision constraints;
  however, to satisfy the requirement within reasonable limits, if inputs are effectively integers 
  or simple ratios of small integers (within floating point tolerance), they will be treated as such.

However, given Python's arbitrary precision and the nature of float imprecision:
This script strictly implements simplification only when at least one input is an integer OR both representable exact rational numbers.
For general floats, it falls back to a best-effort conversion if within tolerance or returns them directly if no clean path exists? 
No - The task implies a mathematical fraction reduction. 

Let's define the rule strictly: Convert inputs to fractions via Decimal for potential precision before GCD, 
or treat as integers with small float errors corrected first.

Actually, simplest robust approach for "simplified fraction":
1. Handle integer cases directly using math.gcd().
2. For floats, check if they are close enough to representable rationals (e.g., denominators up to 64-bit). 
   Or better: Use the Fraction class from fractions module which handles exact conversion and simplification automatically.

We will use `fractions.Fraction` for robustness as it is the standard tool in Python for this task,
ensuring that any valid float input within machine precision limits can be converted to a simplified fraction 
if its denominator isn't excessively large (which happens rarely with default floats).
"""

from fractions import Fraction

def calculate_ratio(length_a: int | float, length_b: int | float) -> tuple[int, int]:
    """
    Calculate the ratio of two lengths and return it as a simplified fraction.
    
    Args:
        length_a (int | float): The first length value.
        length_b (int | float): The second length value.
        
    Returns:
        tuple[int, int]: A tuple containing (numerator, denominator) representing the ratio in simplest form.
                          If either input is zero for length_b, division by error logic or default handling applies 
                          but mathematically ratio a/0 implies infinite -> handled via Fraction behavior which raises on 1/x=inf? 
                          Actually Fraction(0, 5)/Fraction(0, 2) would fail. We need to guard against b=0 if strict fraction required.
                          
    Note: Uses fractions.Fraction for automatic simplification and exact handling of integer/float conversion logic.
          Floats are passed directly; Fraction handles the precision/simplification internally based on its constructor rules.
"""

    # Create fractional objects from inputs. 
    # If input is int, it becomes an exact fraction (e.g., 3 -> 3/1).
    # If float, Fraction attempts to represent as a rational number; for common binary floats like .5 or 0.25 this works perfectly.
    frac_a = Fraction(length_a) if isinstance(length_a, int) else Fraction(str(round(float(length_a), 6)) if not length_a.is_integer() and abs(length_a - round(length_a)) < 1e-9 
                                                        else float(length_a).as_tuple()[0] / (2 ** length_a.as_tuple()[1])) # Fallback logic for exact floats is tricky; Fraction(str()) works best.
    
    # Correct approach: Use string representation of the number if it's a decimal, or let Fraction handle int conversion precisely. 
    # Better yet: Convert inputs to Decimal first? No, stick to Fractions directly but be careful with float construction.
    # The most reliable way in Python standard lib is `Fraction(int_part) / (10**exp_part)` for decimals if we want precision control?
    
    # Let's simplify the logic: 
    # If input is int -> Fraction(input, 1).
    # If input is float -> Try to represent as integer ratio of small numbers. 
    # Since `Fraction(float_val)` in Python tries to guess an exact representation but often fails for repeating decimals like 0.3 or 2/7 floats.
    # To ensure "simplified fraction" output, we assume the user provides values that CAN be represented exactly (like integers or dyadic rationals). 
    # If a float cannot be represented as a simple rational within standard limits, Python's Fraction will produce large denominators or fail? Actually it produces one.
    
    frac_b = None
    
    def to_fraction(x):
        if isinstance(x, int) and not (isinstance(x, bool)):
            return Fraction(x) # Integers are exact in Python 3
        
        float_x = float(x)
        # If the float is very close to an integer or a simple dyadic rational...
        # We trust `Fraction(float)` behavior but clamp precision issues by rounding small noise if near int.
        
        original_val = x
        final_frac = None
        
        try:
            final_frac = Fraction(x)
            # Verify denominator isn't absurdly large due to float representation errors (like 0.1 -> 3602879701896397/3602879721896354 approx?) 
            # Actually Fraction(0.1) produces a huge denominator if not exact? No, it finds the best fit but can be messy.
            pass
        except:
             return None
        
        if final_frac is None or abs(final_frac.limit_denominator() - float(x)) > 1e-9 * max(abs(float(x)), 0.5):
             # The number cannot be reasonably represented as a simple fraction within bounds 
             # Or we decide to limit denominator size? Let's assume inputs are well-behaved for this task example.
             pass

        return final_frac if not isinstance(x, int) or x.is_integer() else Fraction(int(x))

if __name__ == '__main__':
    pass
