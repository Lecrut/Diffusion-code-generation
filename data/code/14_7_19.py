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
    # Sample test cases with hard-coded values
    sample_1 = 50.0
    sample_2 = 49.8

    result = volumes_are_effectively_equal(sample_1, sample_2)
    print(f"Volumes {sample_1} and {sample_2}: {'Equal' if result else 'Not Equal'}")

    # Additional test case with significantly different values
    sample_3 = 50.0
    sample_4 = 60.0

    result_2 = volumes_are_effectively_equal(sample_3, sample_4)
    print(f"Volumes {sample_3} and {sample_4}: {'Equal' if result_2 else 'Not Equal'}")