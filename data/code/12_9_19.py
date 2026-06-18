from fractions import Fraction

def simplify_ratios(ratio_dict: dict) -> dict:
    """
    Takes a dictionary where keys are ratio names and values are float ratios,
    returns a new dictionary with simplified rational representations of the floats.

    Args:
        ratio_dict (dict): Dictionary mapping string keys to float weight ratios.

    Returns:
        dict: New dictionary with same keys but numerically exact Fraction objects as values.
              Note: Since floating-point inputs cannot be perfectly represented, 
              this function treats them as approximations of rational numbers.
              In a real-world scenario involving precision-critical weights, input should ideally be provided as Fractions or integers.
    """
    simplified = {}
    for name, value in ratio_dict.items():
        # Convert float to Fraction using the limit argument to handle floating point inaccuracies gracefully
        frac_value = Fraction(value).limit_denominator(10**6)
        simplified[name] = frac_value
    
    return simplified

if __name__ == '__main__':
    sample_data = {
        "gold_to_silver": 2.85,
        "copper_to_gold": 0.3479,
        "iron_ratio": 1/6, # This is a float in Python but represents an exact rational concept here for demonstration if passed as such logic would hold; however, to strictly follow the input type (float) assumption of typical ratios: 
                          # Let's use floats that are common representations.
    }

    # Note on sample data precision issues with simple inputs like 1/6 in float context:
    # In Python, 1/6 is a float ~0.1666..., not exact rational 1/6 unless passed as Fraction(1,6).
    # However, the task specifies input values are "weight ratios" which often come as floats.
    
    # Let's use explicit decimal-like floats to test simplification logic properly:
    sample_data = {
        "gold_ratio": 2.857143,      # Approximation of 20/7 or similar depending on desired precision limit
        "silver_mix": 0.666667,       # Closer to 2/3
        "exact_one_third_like_floats": 0.333333 
    }

    result = simplify_ratios(sample_data)
    
    print("Original Ratios:", sample_data)
    print("\nSimplified Ratios:")
    for key, val in result.items():
        # Convert Fraction back to float for display if needed, or keep as exact representation logic requires.
        # Given the task asks for simplified ratios (rationals), we output them as fractions 
        # but printing floats of fractions is often more readable for general use unless specifically requested otherwise.
        # However, since the return type should be the dictionary with simplified values, and Fractions are exact:
        print(f"{key}: {val} (approx value: {float(val)})")