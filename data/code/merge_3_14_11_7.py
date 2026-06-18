def compare_volumes(v1: float, v2: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        v1 (float): First volume measurement.
        v2 (float): Second volume measurement.
        
    Returns:
        tuple[float, float, float]: A tuple containing the larger value, 
                                   the smaller value, and their absolute difference.
    """
    if v1 > v2:
        return v1, v2, abs(v1 - v2)
    else:
        return v2, v1, abs(v1 - v2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without external input.
    volume_a = 45000.75
    volume_b = 38924.1

    larger_val, smaller_val, diff = compare_volumes(volume_a, volume_b)
    
    print(f"Larger: {larger_val}")
    print(f"Smaller: {smaller_val}")
    print(f"Difference: {diff:.6f}")