import math

def volumes_are_equal(volume_a: float, volume_b: float) -> bool:
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
    sample_2 = 49.876
    
    result_close = volumes_are_equal(sample_1, sample_2)
    
    sample_3 = 100.0
    sample_4 = 101.5
    
    result_far = volumes_are_equal(sample_3, sample_4)
    
    print(f"Are {sample_1} and {sample_2} equal? {result_close}")
    print(f"Are {sample_3} and {sample_4} equal? {result_far}")