def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        vol1: First floating-point volume measurement.
        vol2: Second floating-point volume measurement.

    Returns:
        A tuple containing the larger value, the smaller value, and their difference.
    """
    if vol1 > vol2:
        return (vol1, vol2, vol1 - vol2)
    else:
        return (vol2, vol1, vol2 - vol1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    v_a = 10.5
    v_b = 7.3
    
    result = compare_volumes(v_a, v_b)
    
    larger_vol, smaller_vol, diff = result
    
    print(f"Larger volume: {larger_vol}")
    print(f"Smaller volume: {smaller_vol}")
    print(f"Difference (absolute): {diff}")