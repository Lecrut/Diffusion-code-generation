def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.
    
    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.
        
    Returns:
        str: Description of the comparison result.
    """
    if abs(volume_a - volume_b) < 1e-9:
        return f"Volumes are equal: {volume_a}"
    elif volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    else:
        return f"{volume_b} is larger than {volume_a}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 5.0
    val2 = 3.7
    
    result = compare_volumes(val1, val2)
    print(result)

    # Additional test case where volumes are equal (using a small float precision example)
    val3 = 10.0
    val4 = 9.999999999
    result_eq = compare_volumes(val3, val4)
    print("Equal comparison:", result_eq)

    # Test case where first is smaller
    val5 = 2.5
    val6 = 7.0
    result_smaller = compare_volumes(val5, val6)
    print(f"Smaller check: {result_smaller}")