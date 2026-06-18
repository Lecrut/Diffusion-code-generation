import math

def volumes_are_close(v1: float, v2: float) -> bool:
    """
    Determines if two volume measurements are effectively equal within a small tolerance.

    Args:
        v1 (float): First volume measurement.
        v2 (float): Second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    
    Note: 
    Uses math.isclose with default relative and absolute tolerances.
    """
    return math.isclose(v1, v2)

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    result1 = volumes_are_close(50.0, 50.0)       # Should be True
    result2 = volumes_are_close(1e-76, 1e-83)     # Should be False (relative difference too large)
    result3 = volumes_are_close(float('inf'), float('inf')) # Should be True
    
    print(f"50.0 vs 50.0: {result1}")      # Expected output: True
    print(f"1e-76 vs 1e-83: {result2}")  # Expected output: False
    print(f"Infinity vs Infinity: {result3}") # Expected output: True