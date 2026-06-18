import math

def volumes_are_effectively_equal(v1: float, v2: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.
    
    Args:
        v1 (float): The first volume measurement.
        v2 (float): The second volume measurement.
        
    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(v1, v2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    vol_a = 50.0
    vol_b = 49.8
    
    result = volumes_are_effectively_equal(vol_a, vol_b)
    
    if result:
        print(f"Volumes {vol_a} and {vol_b} are effectively equal.")
    else:
        print(f"Volumes {vol_a} and {vol_b} are not effectively equal.")