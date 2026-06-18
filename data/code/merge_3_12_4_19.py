import math
from fractions import Fraction

def simplify_ratios(weight_ratios):
    """
    Takes a list of weight ratios (as floats) and returns a new list 
    containing their simplified forms as tuples (numerator, denominator).
    
    Args:
        weight_ratios (list[float]): List of float values representing weights.
        
    Returns:
        list[tuple[int, int]]: List of tuples where each tuple is the 
                               reduced fraction representation of the corresponding input ratio.
    """
    simplified_list = []

    for value in weight_ratios:
        # Handle zero case explicitly to avoid division by zero errors later if needed
        if value == 0:
            simplified_list.append((0, 1))
            continue
        
        # Use Fraction to automatically handle precision issues and find the greatest common divisor
        frac = Fraction(value).limit_denominator()
        
        numerator = frac.numerator
        denominator = frac.denominator
        
        # Ensure positive denominators for consistency (Fraction handles this by default)
        simplified_list.append((numerator, denominator))

    return simplified_list

if __name__ == '__main__':
    # Hard-coded sample values representing weight ratios
    samples = [1.5, 2/3, 0.75, -4.0, 10]
    
    result = simplify_ratios(samples)
    
    print("Input Ratios:", samples)
    print("Simplified Fractions:")
    for i, (num, den) in enumerate(result):
        if num == 0:
            print(f"Ratio {i+1}: 0/1")
        else:
            sign = "-" if num < 0 and den > 0 else ""
            abs_num = abs(num)
            abs_den = abs(den)
            print(f"Ratio {i+1}: {sign}{abs_num}/{abs_den}")