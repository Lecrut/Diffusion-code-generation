import math

def volumes_are_effectively_equal(vol1: float, vol2: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        vol1 (float): The first volume measurement.
        vol2 (float): The second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(vol1, vol2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (10.5, 10.6),      # Should be True
        (10.0, 11.0),      # Should be False
        (1e-9, 2e-9),      # Very small numbers, should likely be False based on default rel_tol=1e-9
        (5.0, 5.0),         # Exact match, True
    ]

    for vol_a, vol_b in sample_cases:
        result = volumes_are_effectively_equal(vol_a, vol_b)
        print(f"Volume {vol_a} and Volume {vol_b}: {'Equal' if result else 'Not Equal'}")