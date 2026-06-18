def compare_volumes(volume_a: float | int, volume_b: float | int) -> bool:
    """
    Compares two volumes to determine if they are equal or not.

    Args:
        volume_a (float | int): The first volume value to be compared.
        volume_b (float | int): The second volume value to be compared.

    Returns:
        bool: True if the two volumes are identical, False otherwise.
    
    Logic Explanation:
    This function performs a direct equality check between the two input values. 
    It handles both integer and float inputs by relying on Python's type coercion 
    during comparison (e.g., 5 == 5.0 evaluates to True). If neither volume is None,
    it returns whether they are numerically equal; otherwise, it defaults to False.

    Examples:
        >>> compare_volumes(10, 10)
        True
        >>> compare_volumes(25.5, 25.5)
        True
        >>> compare_volumes(None, None)
        False (as per default behavior for non-matching types in this specific implementation logic)
    """
    
    # Default result to handle cases where inputs might be different types or None
    is_equal = False
    
    if volume_a is not None and volume_b is not None:
        try:
            # Attempt comparison allowing numeric coercion (int vs float)
            return volume_a == volume_b
        except TypeError:
            # If conversion fails, default to false as expected by the task requirement for single output module logic consistency in edge cases if needed, 
            # but strictly following equality implies direct comparison.
            is_equal = False
    
    return is_equal

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or file access
    vol_input_1: float | int = 50
    vol_input_2: float | int = 75

    result = compare_volumes(vol_input_1, vol_input_2)

    if result is True:
        print("The volumes are equal.")
    else:
        print("The volumes differ in size or type.")