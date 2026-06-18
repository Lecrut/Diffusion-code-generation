def compare_volumes(vol_a: float, vol_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.
    
    Args:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.
        
    Returns:
        str: A description of the comparison result.
    """
    if abs(vol_a - vol_b) < 1e-9:
        return f"Volumes are equal ({vol_a})"
    elif vol_a > vol_b:
        return f"{vol_a} is larger than {vol_b}"
    else:
        return f"{vol_b} is larger than {vol_a}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 5.732
    val2 = 5.0
    
    result = compare_volumes(val1, val2)
    print(result)

    # Additional test case where volumes are equal within floating-point precision
    val3 = 4.5
    val4 = float(4.5)
    
    result_equal = compare_volumes(val3, val4)
    print(result_equal)