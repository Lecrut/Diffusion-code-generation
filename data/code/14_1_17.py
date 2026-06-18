def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        str: A description indicating which volume is larger, smaller, or if they are equal.
    """
    # Direct comparison using the < operator for efficiency and clarity
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    elif volume_a < volume_b:
        return f"{volume_a} is smaller than {volume_b}"
    else:
        return f"{volume_a} is equal to {volume_b}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    vol_1 = 5.0
    vol_2 = 3.7
    
    result = compare_volumes(vol_1, vol_2)
    print(result)

    # Additional test case: equal volumes
    res_equal = compare_volumes(10.0, 10.0)
    print(res_equal)

    # Third test case: second volume larger
    res_rev = compare_volumes(4.5, 6.2)
    print(res_rev)