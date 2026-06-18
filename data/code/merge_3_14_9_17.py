"""
Module to compare two volume inputs with type hinting and clear documentation.

This module defines a function that takes two numeric volumes, compares their magnitudes,
and returns an integer indicating which is larger or if they are equal. It uses Python's
type hints for clarity on expected input types and return values. The comparison logic
is encapsulated within the `compare_volumes` function with comprehensive docstrings explaining
the behavior of each branch in the conditional statement.

The module includes a main execution block that demonstrates usage with hard-coded sample values,
ensuring it runs without any user interaction or external dependencies.
"""

def compare_volumes(volume_a: float | int, volume_b: float | int) -> int:
    """
    Compare two volumes and return the result of their comparison as an integer.

    This function accepts two numeric values representing volumes (integers or floats).
    It performs a standard magnitude comparison between them and returns 1 if the first
    argument is strictly greater, -1 if it is strictly less, and 0 if they are equal.

    Args:
        volume_a (float | int): The first volume value to compare. Can be an integer or float.
        volume_b (float | int): The second volume value to compare. Must match the type of volume_a for consistency.

    Returns:
        int: An integer result indicating the comparison outcome:
             - 1 if volume_a > volume_b
             - -1 if volume_a < volume_b
             - 0 if volume_a == volume_b

    Raises:
        TypeError: If either input is not a numeric type (int or float).

    Example:
        >>> compare_volumes(5, 3)
        1
        >>> compare_volumes(2.5, 2.5)
        0
        >>> compare_volumes(10, 7)
        -1
    """
    
    # Validate input types to ensure only numeric values are processed
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")

    # Perform the comparison logic using standard operators for clarity and efficiency
    if volume_a > volume_b:
        return 1
    elif volume_a < volume_b:
        return -1
    
    # If neither condition is met, the values are equal
    return 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    # These represent two distinct volumes for testing purposes.
    SAMPLE_VOLUME_A = 500
    SAMPLE_VOLUME_B = 750
    
    result = compare_volumes(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)
    
    print(f"Comparing {SAMPLE_VOLUME_A} and {SAMPLE_VOLUME_B}:")
    if result == 1:
        print("The first volume is larger.")
    elif result == -1:
        print("The second volume is larger.")
    else:
        print("Both volumes are equal.")