def compare_volumes(v1: float, v2: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        v1: First floating-point volume measurement.
        v2: Second floating-point volume measurement.
        
    Returns:
        A tuple containing the larger value, the smaller value, and their absolute difference.
    """
    if v1 > v2:
        return (v1, v2, abs(v1 - v2))
    else:
        return (v2, v1, abs(v1 - v2))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    vol_a = 10.5
    vol_b = 7.3
    
    larger, smaller, diff = compare_volumes(vol_a, vol_b)
    
    print(f"Larger volume: {larger}")
    print(f"Smaller volume: {smaller}")
    print(f"Difference: {diff}")