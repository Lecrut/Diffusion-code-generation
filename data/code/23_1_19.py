def compare_and_report(a: int | float, b: int | float) -> dict:
    """
    Compares two numerical values (integers or floats), calculates their difference
    and ratio of the larger to the smaller value. Returns a dictionary with these results.
    
    Args:
        a (int | float): First numerical value.
        b (int | float): Second numerical value.
        
    Returns:
        dict: A dictionary containing 'larger', 'smaller', 'difference' (rounded to 6 decimals), 
              and 'ratio'. Handles zero cases gracefully for ratio calculation by returning None or infinity logic if needed,
              but per standard math rules, avoids division by zero in the final report unless explicitly handled.
    """
    larger = max(a, b)
    smaller = min(a, b)
    
    difference = abs(larger - smaller)
    
    # Avoid division by zero for ratio if one value is exactly zero and it's the smaller
    if smaller == 0:
        ratio = float('inf') if larger != 0 else None
    elif larger == 0:
        ratio = 1.0
    else:
        ratio = larger / smaller
    
    return {
        'larger': larger,
        'smaller': smaller,
        'difference': round(difference, 6),
        'ratio': ratio if isinstance(ratio, (int, float)) and not isinstance(ratio, bool) else None # Ensure boolean isn't passed through as valid number type in some contexts though floats are fine. Actually simple check: just return the calculated value. If inf is returned it's a float.
    }

if __name__ == '__main__':
    sample_cases = [
        (10, 5),
        (-3.5, -7.2),
        (0, 42),
        (42, 0),
        (0, 0)
    ]

    for val_a, val_b in sample_cases:
        result = compare_and_report(val_a, val_b)
        print(f"Comparing {val_a} and {val_b}:")
        print(result)