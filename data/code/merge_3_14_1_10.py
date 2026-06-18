def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        str: Description of the comparison result.
    """
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    elif volume_a < volume_b:
        return f"{volume_a} is smaller than {volume_b}"
    else:
        return f"{volume_a} and {volume_b} are equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    vol1 = 5.7
    vol2 = 3.2
    
    result = compare_volumes(vol1, vol2)
    print(result)

    # Additional test case where volumes are equal
    eq_result = compare_volumes(4.0, 4.0)
    print(eq_result)

    # Test case where first volume is smaller
    lt_result = compare_volumes(1.5, 9.8)
    print(lt_result)