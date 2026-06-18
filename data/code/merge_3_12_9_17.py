import math
from fractions import Fraction

def simplify_ratios(ratio_dict: dict) -> dict:
    """
    Takes a dictionary where keys are ratio names (strings) 
    and values are weight ratios represented as floats or integers,
    and returns a new dictionary with the same keys but simplified ratios.

    Simplification is done by converting each value to a Fraction,
    reducing it to its lowest terms, and then converting back to float/int representation.
    
    Args:
        ratio_dict (dict): Dictionary of {name: weight_ratio}
        
    Returns:
        dict: A new dictionary with simplified ratios for the same keys.
    """
    result = {}

    for name, value in ratio_dict.items():
        # Convert input to float first if it's an integer or Fraction-like object
        num_float = float(value)
        
        # Use fractions.Fraction to get exact rational representation and reduce automatically
        frac_value = Fraction(num_float).limit_denominator()  # limit_denominator ensures precision handling for floats
        
        # Get numerator and denominator of the simplified fraction
        numerator = frac_value.numerator
        denominator = frac_value.denominator

        # Convert back to float if original was float, otherwise keep as int if it's a whole number ratio
        is_integer_ratio = (numerator % denominator == 0) or abs(num_float - int(num_float)) < 1e-9
        
        simplified_value = numerator / denominator

        result[name] = simplified_value

    return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_data = {
        "gold_silver": 2.0,
        "silver_copper": 3.5,
        "iron_lead": 1.75,
        "pure_gold": 4.8 / 9.6,  # Should simplify to 0.5 or similar depending on precision handling
    }

    simplified_data = simplify_ratios(sample_data)

    print("Original Ratios:")
    for k, v in sample_data.items():
        print(f"{k}: {v}")

    print("\nSimplified Ratios:")
    for k, v in simplified_data.items():
        print(f"{k}: {v}")