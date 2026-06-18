def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        vol1: First floating-point volume measurement.
        vol2: Second floating-point volume measurement.
        
    Returns:
        A tuple containing the larger volume, the smaller volume, 
        and their absolute difference as floats.
    """
    if vol1 > vol2:
        larger = vol1
        smaller = vol2
    else:
        larger = vol2
        smaller = vol1
    
    return (larger, smaller, abs(larger - smaller))

if __name__ == '__main__':
    sample_vol_a = 50.75
    sample_vol_b = 38.2
        
    result_large, result_small, result_diff = compare_volumes(sample_vol_a, sample_vol_b)
    
    print(f"Larger volume: {result_large}")
    print(f"Smaller volume: {result_small}")
    print(f"Difference: {result_diff}")