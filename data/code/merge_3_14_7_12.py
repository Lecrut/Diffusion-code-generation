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
    # Hard-coded sample values for testing without user input or files
    vol_1 = 3.0
    vol_2 = 3.5
    
    result = volumes_are_effectively_equal(vol_1, vol_2)
    
    if result:
        print("The volumes are effectively equal.")
    else:
        print("The volumes are not effectively equal.")