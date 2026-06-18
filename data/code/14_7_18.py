import math

def volumes_are_equal(vol1: float, vol2: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(vol1, vol2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_vol_1 = 50.0
    sample_vol_2 = 49.8

    result = volumes_are_equal(sample_vol_1, sample_vol_2)
    print(f"Volumes {sample_vol_1} and {sample_vol_2}: {'Equal' if result else 'Not Equal'}")