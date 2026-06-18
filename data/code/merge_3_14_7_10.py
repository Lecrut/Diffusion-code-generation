import math

def volumes_are_effectively_equal(volume_a: float, volume_b: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(volume_a, volume_b)

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    
    # Test case 1: Clearly different values (should be False)
    vol_1 = 50.0
    vol_2 = 60.0
    result_1 = volumes_are_effectively_equal(vol_1, vol_2)

    # Test case 2: Identical values (should be True)
    val_a = 100.0
    val_b = 100.0
    result_2 = volumes_are_effectively_equal(val_a, val_b)

    # Test case 3: Values very close to each other within default tolerance (should be True)
    vol_c = 98.54321
    vol_d = 98.55000
    result_3 = volumes_are_effectively_equal(vol_c, vol_d)

    # Test case 4: Values slightly outside default relative and absolute tolerance (should be False)
    val_e = 1e-6
    val_f = 2e-6
    result_4 = volumes_are_effectively_equal(val_e, val_f)

    print(f"Test 1 ({vol_1} vs {vol_2}): {result_1}")
    print(f"Test 2 ({val_a} vs {val_b}): {result_2}")
    print(f"Test 3 ({vol_c} vs {vol_d}): {result_3}")
    print(f"Test 4 ({val_e} vs {val_f}): {result_4}")