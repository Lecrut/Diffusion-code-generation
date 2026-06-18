import math
from fractions import Fraction

def simplify_ratios(ratios_dict):
    """
    Takes a dictionary where keys are ratio names and values are numeric weight ratios,
    returns a new dictionary with all values simplified to their lowest terms as floats.

    Args:
        ratios_dict (dict): Dictionary mapping string keys to float/numeric ratio values.

    Returns:
        dict: A new dictionary with the same keys but simplified float values.
    
    Note: Simplification is performed by dividing both numerator and denominator 
    of each fraction by their greatest common divisor, then converting back to float.
    """
    result = {}
    for name, value in ratios_dict.items():
        # Handle integer inputs directly
        if isinstance(value, int):
            simplified_value = float(value) / 100.0
        else:
            # Convert to Fraction for precise simplification
            fraction = Fraction(int(round(value * 100)), 100).limit_denominator(10**9)
            simplified_value = float(fraction.numerator) / float(fraction.denominator)
        
        result[name] = simplified_value
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values representing weight ratios in percentages
    raw_ratios = {
        "gold": 58.3,
        "silver": 41.7,
        "copper": 20.5,
        "iron": 60.0,
        "lead": 99.9
    }

    simplified_ratios = simplify_ratios(raw_ratios)

    print("Original Ratios:")
    for k, v in raw_ratios.items():
        print(f"{k}: {v}%")

    print("\nSimplified Ratios (normalized to base 100):")
    for k, v in simplified_ratios.items():
        # Round to reasonable precision for display
        rounded_v = round(v, 5)
        if not math.isclose(rounded_v, int(rounded_v), rel_tol=1e-9):
            print(f"{k}: {rounded_v}")
        else:
            print(f"{k}: {int(rounded_v)}")

    # Verify that the simplified values are consistent representations of simple fractions
    assert abs(simplified_ratios["gold"] - 0.583) < 1e-9, "Gold ratio mismatch"
    assert abs(simplified_ratios["iron"] - 0.6) < 1e-9, "Iron ratio mismatch"