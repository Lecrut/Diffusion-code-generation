def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        vol1: First floating-point volume measurement.
        vol2: Second floating-point volume measurement.
        
    Returns:
        A tuple containing the larger value, the smaller value, and their absolute difference.
    """
    if vol1 > vol2:
        return (vol1, vol2, abs(vol1 - vol2))
    else:
        return (vol2, vol1, abs(vol1 - vol2))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    volume_a = 5.734
    volume_b = 8.092
    
    larger, smaller, diff = compare_volumes(volume_a, volume_b)
    
    print(f"Larger Volume: {larger}")
    print(f"Smaller Volume: {smaller}")
    print(f"Difference: {diff}")