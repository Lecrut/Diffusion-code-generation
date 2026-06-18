def compare_volumes(vol_a: float, vol_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.
    
    Args:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.
        
    Returns:
        str: A description of the relationship between the volumes.
    """
    if abs(vol_a - vol_b) < 1e-9:
        return f"Volume {vol_a} is equal to Volume {vol_b}"
    
    comparison = "smaller than" if vol_a < vol_b else "larger than"
    return f"Volume {vol_a} is {comparison} Volume {vol_b}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    volume_1 = 5.0
    volume_2 = 3.7
    
    result = compare_volumes(volume_1, volume_2)
    print(result)

    # Additional test case: equal volumes
    vol_equal_a = 10.0
    vol_equal_b = 10.0
    res_eq = compare_volumes(vol_equal_a, vol_equal_b)
    print(res_eq)

    # Test case where first is larger
    vol_large_first = 25.5
    vol_small_second = 9.9
    res_larger = compare_volumes(vol_large_first, vol_small_second)
    print(res_larger)