"""
Module to compare two volume inputs based on magnitude.

This module provides a function that takes two numeric values representing volumes,
compares their magnitudes (absolute value), and returns the larger of the two.
The comparison logic is robust against negative numbers by using absolute values.

Type hints are used for clarity in argument types and return type.
Docstrings explain the purpose, parameters, and behavior of functions.
"""

def compare_volumes(volume_a: float | int, volume_b: float | int) -> float | int:
    """
    Compares two volumes based on their magnitude (absolute value).

    This function determines which input has a larger absolute value.
    If the magnitudes are equal, it returns the first argument unchanged.
    Negative numbers are handled correctly by comparing their absolute values.

    Args:
        volume_a: The first numeric volume to compare. Can be int or float.
        volume_b: The second numeric volume to compare. Can be int or float.

    Returns:
        The value with the larger magnitude (absolute value).
        If |volume_a| >= |volume_b|, returns volume_a; otherwise, returns volume_b.

    Examples:
        >>> compare_volumes(10, 5)
        10
        >>> compare_volumes(-20, -30)
        -30
        >>> compare_volumes(0, 0)
        0
    """
    if abs(volume_a) >= abs(volume_b):
        return volume_a
    return volume_b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    SAMPLE_VOLUME_A = -50.5
    SAMPLE_VOLUME_B = 75

    result_volume = compare_volumes(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)

    print(f"Comparing volumes: {SAMPLE_VOLUME_A} and {SAMPLE_VOLUME_B}")
    print(f"The volume with the larger magnitude is: {result_volume}")