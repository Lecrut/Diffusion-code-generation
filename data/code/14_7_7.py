import math

def volumes_equal(v1: float, v2: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.
    
    Args:
        v1 (float): First volume measurement.
        v2 (float): Second volume measurement.
        
    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(v1, v2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values that require no user input or external resources
    
    result_1 = volumes_equal(500.0, 498.76)
    
    result_2 = volumes_equal(100.0, 101.3)
    
    print(result_1)
    print(result_2)