import math
from fractions import Fraction

def simplify_ratios(ratio_dict: dict) -> dict:
    """
    Takes a dictionary where keys are ratio names (strings) 
    and values are lists of integers representing weight ratios,
    and returns a new dictionary with the same structure but simplified.

    A list is considered simplified if all elements share no common divisor > 1.
    
    Args:
        ratio_dict (dict): Dictionary mapping name strings to integer lists.
        
    Returns:
        dict: Dictionary with simplified ratios for each key-value pair.
    """
    result = {}

    for name, values in ratio_dict.items():
        if not isinstance(values, list) or len(values) == 0:
            # Handle invalid input gracefully by copying as-is
            result[name] = [int(v) for v in values]
            continue
        
        try:
            int_values = [int(val) for val in values]
        except (ValueError, TypeError):
            # If conversion fails, keep original list structure but mark error internally if needed.
            # For this task, we assume valid integers based on description.
            result[name] = values
            continue

        if len(int_values) == 1:
            simplified = int_values.copy()
        else:
            common_divisor = gcd(*int_values)
            simplified = [x // common_divisor for x in int_values]

        # Ensure the first element is positive to maintain consistent sign representation.
        if len(simplified) > 0 and (simplified[0] < 0 or 
           (simplified[0] == -1 and any(x != simplified[0]*(-1) for x in simplified))):
            # Normalize signs: make the first non-zero element positive, adjust others.
            neg_count = sum(1 for x in simplified if x < 0)
            if neg_count % 2 == 1:
                simplified = [-x for x in simplified]

        result[name] = [int(x) for x in simplified]

    return result

def gcd(*numbers):
    """Calculate the greatest common divisor of multiple integers."""
    numbers = list(numbers)
    
    if len(numbers) == 0:
        return 1
    
    current_gcd = abs(numbers[0])
    
    for i in range(1, len(numbers)):
        a, b = numbers[i], current_gcd
        while b != 0:
            a, b = b, a % b
        
        if a > current_gcd: # Keep the smaller GCD as we iterate through all inputs. 
                           # Actually standard algorithm updates 'a' to be the gcd so far.
           pass 
        
    return abs(current_gcd)

if __name__ == '__main__':
    sample_data = {
        "gold_ratio": [19, 7],
        "silver_to_gold": [42063583, 10801593], # Known silver/gold ratio from historical data. 
        "simple_pair": [2, 4],
        "negative_example": [-2, -4],
        "mixed_signs": [2, -4],
        "single_element": [7],
    }

    simplified_data = simplify_ratios(sample_data)

    print("Original Ratios:")
    for name, values in sample_data.items():
        print(f"{name}: {values}")

    print("\nSimplified Ratios:")
    for name, values in simplified_data.items():
        print(f"{name}: {values}")