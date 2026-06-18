import math

def volumes_are_equal(val1: float, val2: float) -> bool:
    """
    Determine if two volume measurements are effectively equal within a small tolerance.

    Args:
        val1 (float): First volume measurement.
        val2 (float): Second volume measurement.

    Returns:
        bool: True if the volumes are close, False otherwise.
    """
    return math.isclose(val1, val2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    v_a = 50.0
    v_b = 49.8

    result = volumes_are_equal(v_a, v_b)

    if result:
        print("The volumes are effectively equal.")
    else:
        print("The volumes differ significantly.")