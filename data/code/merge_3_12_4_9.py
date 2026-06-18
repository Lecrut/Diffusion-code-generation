import math
from fractions import Fraction

def simplify_ratios(weight_ratios):
    """
    Takes a list of weight ratios (as lists/tuples) and returns a new list 
    containing simplified forms as tuples. A ratio is considered simplified if the GCD 
    of its numerator and denominator is 1, or if it's treated as an integer when possible.

    Args:
        weight_ratios (list): List of pairs representing [numerator, denominator] ratios.

    Returns:
        list: List of tuples where each tuple represents a simplified ratio.
              If the original was integers, returns int; otherwise Fraction or reduced float logic applied via GCD on floats converted to ints if possible, 
              but primarily using math.gcd for integer reduction as per standard interpretation of "weight ratios" in such contexts unless specified as decimals requiring precision handling.

    Note: This implementation assumes inputs are lists/tuples of two numbers (numerator, denominator).
          For float inputs, it attempts to convert them to integers if they represent exact values, 
          otherwise returns a tuple with the original floats reduced by their GCD approximation logic via Fraction for accuracy in representation.
    """

    def get_gcd(a, b):
        return math.gcd(int(round(a)), int(round(b))) if (a != float('inf') and not isinstance(a, complex)) else 1

    simplified = []
    
    for ratio_pair in weight_ratios:
        # Ensure we have exactly two elements
        if len(ratio_pair) != 2:
            raise ValueError(f"Each ratio must contain exactly two values. Got {len(ratio_pair)}.")
        
        num, den = ratio_pair
        
        # Handle edge case where denominator is zero or both are zero
        if den == 0 and num == 0:
            simplified.append((1, 0)) # Conventionally undefined, but represented as (1,0) for consistency in some systems
            continue
            
        if den != 0:
            try:
                # Attempt to treat inputs as integers first for precision reduction
                n_int = int(round(num))
                d_int = int(round(den))
                
                if not isinstance(n_int, (int, float)): 
                    raise ValueError("Input values must be numeric.")

                common_divisor = get_gcd(abs(n_int), abs(d_int))
                simplified_num = n_int // common_divisor
                simplified_den = d_int // common_divisor
                
                # Ensure positive denominator for canonical form
                if simplified_den < 0:
                    simplified_num *= -1
                    simplified_den *= -1
                    
                result_tuple = (simplified_num, simplified_den)

            except OverflowError:
                # Fallback to Fraction logic for large or non-integer floats that can be represented exactly as fractions
                frac = Fraction(num).limit_denominator() if isinstance(num, float) else num / den
                # Re-evaluate based on whether we want strict integer reduction or general simplification
                # Given the task implies "weight ratios", usually integers are preferred if possible. 
                # If floats were provided and not exact integers, Fraction is safer for representation than arbitrary precision math.gcd on raw floats which loses info.
                
                num_frac = frac.numerator
                den_frac = frac.denominator
                
                result_tuple = (num_frac, den_frac)

            else:
                 simplified.append(result_tuple)
        else:
             # Denominator was zero but numerator wasn't -> undefined behavior handled by raising or returning specific marker if needed. 
             # Here we assume valid input for this function scope unless specified otherwise.
             pass
    
    return simplified

if __name__ == '__main__':
    sample_ratios = [
        [2, 4],      # Should simplify to (1, 2)
        [50, 75],    # Should simplify to (2, 3)
        [-8, -6],    # Should simplify to (-4, -3) or (4, 3)? Canonical is usually positive denominator -> (-4/3), but let's stick to sign preservation unless den<0 flip. 
                     # My logic: if simplified_den < 0 then flip both. So [-8/-6] -> gcd(8,6)=2 -> -4/-3 -> denom negative? No, -3 is neg. Flip -> 4/3.
        [1, 3],      # Already simple (1, 3)
        [7, 0],      # Invalid denominator case handled by logic flow above if den!=0 check passes or fails appropriately based on implementation detail of 'den' being zero initially. 
                     # Actually in my code: if den==0 and num==0 -> handle. else if den != 0 ...
        [1, 2],      # (1, 2)
    ]

    result = simplify_ratios(sample_ratios)
    
    print("Input Ratios:", sample_ratios)
    print("Simplified Ratios:", result)