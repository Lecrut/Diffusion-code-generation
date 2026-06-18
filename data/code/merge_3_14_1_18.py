def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        str: A description of the relationship between the volumes.
    """
    if abs(volume_a - volume_b) < 1e-9:
        return f"{volume_a} and {volume_b} are equal."
    
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}."
    else:
        return f"{volume_b} is larger than {volume_a}."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    val1 = 50.75
    val2 = 49.8
    
    result = compare_volumes(val1, val2)
    print(result)

    # Additional test case where volumes are equal (within float precision limits).
    val3 = 10.0
    val4 = 10.0
    result_equal = compare_volumes(val3, val4)
    print(result_equal)