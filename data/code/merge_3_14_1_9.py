def compare_volumes(vol1: float, vol2: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.

    Returns:
        str: A description of the comparison result ('vol1 is larger', 'vol2 is larger', or 'volumes are equal').
    """
    if vol1 > vol2:
        return "Volume 1 is larger"
    elif vol2 > vol1:
        return "Volume 2 is larger"
    else:
        return "Volumes are equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    v_a = 5.0
    v_b = 3.7
    
    result = compare_volumes(v_a, v_b)
    
    print(f"Comparing {v_a} and {v_b}:")
    print(result)