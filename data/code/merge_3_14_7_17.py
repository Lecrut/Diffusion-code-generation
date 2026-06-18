import math

def volumes_are_effectively_equal(volume_a: float, volume_b: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(volume_a, volume_b)

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    vol_1 = 50.0
    vol_2 = 49.8
    
    result = volumes_are_effectively_equal(vol_1, vol_2)
    
    print(f"Volume A: {vol_1}")
    print(f"Volume B: {vol_2}")
    print(f"Are they effectively equal? {result}")