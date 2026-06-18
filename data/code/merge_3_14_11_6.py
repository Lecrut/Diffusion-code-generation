def compare_volumes(vol_a: float, vol_b: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        vol_a: First floating-point volume measurement.
        vol_b: Second floating-point volume measurement.
        
    Returns:
        A tuple containing the larger value, the smaller value, and their difference.
    """
    if vol_a > vol_b:
        return (vol_a, vol_b, abs(vol_a - vol_b))
    else:
        return (vol_b, vol_a, abs(vol_a - vol_b))

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    val1 = 250.75
    val2 = 300.4
    
    result = compare_volumes(val1, val2)
    
    print(f"Larger Volume: {result[0]}")
    print(f"Smaller Volume: {result[1]}")
    print(f"Difference: {result[2]}")