import math

def volumes_are_effectively_equal(vol_a: float, vol_b: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        vol_a (float): The first volume measurement.
        vol_b (float): The second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(vol_a, vol_b)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_1 = 10.5
    sample_2 = 10.5
    
    result_close = volumes_are_effectively_equal(sample_1, sample_2)

    print(f"Are {sample_1} and {sample_2} effectively equal?")
    print(result_close)