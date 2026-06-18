def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        str: Description of the comparison result ("a is larger", "b is larger", or "they are equal").
    """
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    elif volume_b > volume_a:
        return f"{volume_b} is larger than {volume_a}"
    else:
        return f"Volumes are equal ({volume_a})"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    vol1 = 50.7
    vol2 = 49.3
    
    result = compare_volumes(vol1, vol2)
    
    print(result)