import sys

def compare_volumes(vol_a: float, vol_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.

    Args:
        vol_a (float): First volume measurement.
        vol_b (float): Second volume measurement.

    Returns:
        str: Description of the relationship between the volumes.
    """
    if vol_a == vol_b:
        return f"{vol_a} is equal to {vol_b}"
    elif vol_a > vol_b:
        return f"{vol_a} is larger than {vol_b}"
    else:
        return f"{vol_a} is smaller than {vol_b}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI arguments.
    sample_vol_1 = 50.7
    sample_vol_2 = 50.7
    
    result = compare_volumes(sample_vol_1, sample_vol_2)
    
    print(result)