import sys

def compare_volumes(volume_a: float | int, volume_b: float | int) -> bool:
    """
    Compares two volume inputs to determine if they are equal.

    This function takes two numeric values representing volumes and returns True
    if the first value is strictly greater than the second, False otherwise.
    
    Args:
        volume_a (float | int): The first volume input. Supports both integers 
                                and floats due to type hinting allowing union types.
        volume_b (float | int): The second volume input. Also supports both 
                                integer and float values for comparison.

    Returns:
        bool: True if `volume_a` > `volume_b`, False otherwise.

    Raises:
        TypeError: If either argument is not a numeric type supported by the function.
    
    Example:
        >>> compare_volumes(10, 5)
        True
        >>> compare_volumes(3.5, 4.2)
        False
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be numeric types (int or float).")

    return volume_a > volume_b

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    SAMPLE_VOLUME_A = 100
    SAMPLE_VOLUME_B = 50

    result = compare_volumes(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)

    print(f"Comparing {SAMPLE_VOLUME_A} with {SAMPLE_VOLUME_B}:")
    if result:
        print("Result: Volume A is greater.")
    else:
        print("Result: Volume A is not greater than Volume B.")