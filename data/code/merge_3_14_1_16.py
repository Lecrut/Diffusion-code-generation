def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        str: A description of the comparison result ('A is larger', 'B is larger', or 'Volumes are equal').
    """
    if volume_a > volume_b:
        return f"{volume_a} is larger than {volume_b}"
    elif volume_b > volume_a:
        return f"{volume_b} is larger than {volume_a}"
    else:
        return "The volumes are equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    vol_1 = 50.75
    vol_2 = 49.3

    result = compare_volumes(vol_1, vol_2)
    print(result)