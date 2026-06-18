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
    # Hard-coded sample values for testing without user input or external dependencies.
    measurement_a = 150.75
    measurement_b = 89.3

    result_larger, result_smaller, result_diff = compare_volumes(measurement_a, measurement_b)

    print(f"Larger volume: {result_larger}")
    print(f"Smaller volume: {result_smaller}")
    print(f"Difference: {result_diff}")