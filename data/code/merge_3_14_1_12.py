def compare_volumes(vol_a: float, vol_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.

    Returns:
        str: Description of the relationship between the volumes.
    """
    if vol_a > vol_b:
        return f"{vol_a} is larger than {vol_b}"
    elif vol_b > vol_a:
        return f"{vol_b} is larger than {vol_a}"
    else:
        return f"{vol_a} and {vol_b} are equal"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    vol_1 = 5.0
    vol_2 = 3.7

    result = compare_volumes(vol_1, vol_2)
    print(result)