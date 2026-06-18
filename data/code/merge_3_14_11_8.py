def compare_volumes(vol_a: float, vol_b: float) -> tuple[float, float, float]:
    """
    Returns a tuple containing (larger_volume, smaller_volume, absolute_difference).
    
    Parameters:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.
        
    Returns:
        tuple: A 3-element tuple of the larger value, smaller value, and their difference.
    """
    if vol_a > vol_b:
        return vol_a, vol_b, vol_a - vol_b
    else:
        return vol_b, vol_a, vol_b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_vol_1 = 15.7
    sample_vol_2 = 8.3
    
    result_large, result_small, diff = compare_volumes(sample_vol_1, sample_vol_2)
    
    print(f"Larger: {result_large}")
    print(f"Smaller: {result_small}")
    print(f"Difference: {diff}")