def compare_volumes(vol_a: float, vol_b: float) -> dict[str]:
    """
    Compare two volume measurements and return a dictionary with 
    comparison results.

    Args:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.

    Returns:
        dict containing:
            - 'vol_a': The first input volume
            - 'vol_b': The second input volume
            - 'ratio': Ratio of the larger to the smaller volume
            - 'equal': Boolean indicating if both volumes are equal
    """
    
    # Determine which is larger and calculate ratio
    if vol_a >= vol_b:
        numerator, denominator = vol_a, vol_b if vol_b != 0 else float('inf')
    else:
        numerator, denominator = vol_b, vol_a if vol_a != 0 else float('inf')

    # Handle division by zero case explicitly for clarity
    ratio = num / denom
    
    return {
        'vol_a': vol_a,
        'vol_b': vol_b,
        'ratio': ratio,
        'equal': False
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    result = compare_volumes(10.5, 2.3)
    
    print("Volume Comparison Result:")
    for key in ['vol_a', 'vol_b', 'ratio', 'equal']:
        if isinstance(result[key], float):
            # Format floats to avoid excessive decimal places unless integer-like
            formatted = f"{result[key]:g}" if int(round(result[key]) == result[key]) else str(result[key])
        else:
            formatted = repr(result[key])
        
        print(f"  {key}: {formatted}")