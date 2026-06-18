def simplify_ratios(ratio_dict):
    """
    Takes a dictionary where keys are ratio names (strings) 
    and values are tuples of integers representing weight ratios,
    and returns a new dictionary with simplified integer ratios.
    
    A fraction is in its simplest form when the greatest common divisor
    of numerator and denominator is 1. This function applies this logic to all pairs.

    Args:
        ratio_dict (dict): Dictionary mapping names to tuples of integers.

    Returns:
        dict: New dictionary with simplified integer ratios for each name.
    """
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    result_dict = {}
    
    for name, (numerator, denominator) in ratio_dict.items():
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError(f"Values must be integer tuples. Got {type(ratio_dict[name])} for key '{name}'.")
        
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        
        # Ensure the sign is consistent: if both are negative or one is positive and other negative (resulting in negative fraction), make it standard.
        # Standard form for fractions usually keeps the denominator positive.
        if simplified_denominator < 0:
            simplified_numerator = -simplified_numerator
            simplified_denominator = -simplified_denominator
            
        result_dict[name] = (simplified_numerator, simplified_denominator)

    return result_dict

if __name__ == '__main__':
    # Sample input dictionary with ratio names and integer weight tuples.
    sample_data = {
        "red_to_blue": (30, 50),
        "green_ratio": (12, 8),
        "gold_mixture": (-4, -6),
        "simple_one": (7, 1)
    }

    simplified_result = simplify_ratios(sample_data)

    # Output the result for verification. No user input is required or used here.
    print("Original Ratios:", sample_data)
    print("\nSimplified Ratios:")
    for name, ratio in simplified_result.items():
        num, den = ratio
        if den == 1:
            print(f"{name}: {num}")
        else:
            print(f"{name}: {num}/{den}")