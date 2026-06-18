"""
Module to compare two volume values numerically.

This module provides a function that takes two numeric inputs representing volumes,
compares their magnitudes, and returns the larger value along with a descriptive message.
It utilizes type hinting for clarity on expected input types and return structure.
The comparison logic is straightforward: if the first argument is greater than or equal to
the second, it is returned; otherwise, the second argument is returned.

Functions defined here are designed to be stateless and deterministic.
"""

def compare_volumes(volume_a: float | int, volume_b: float | int) -> tuple[float | int, str]:
    """
    Compare two volumes and return the larger one with a status message.

    This function accepts two numeric values representing volumes (integers or floats).
    It determines which value is greater numerically and returns them in an ordered tuple.
    The second element of the tuple provides a clear textual explanation of the result,
    indicating whether volume A was larger than B or if they were equal.

    Parameters:
        volume_a (float | int): The first numeric input representing a volume quantity.
        volume_b (float | int): The second numeric input representing a volume quantity.

    Returns:
        tuple[float | int, str]: A tuple containing two elements:
            1. The larger of the two volumes (or either if equal).
            2. A descriptive string explaining the comparison outcome in English.

    Raises:
        TypeError: If either input is not a number (int or float).

    Examples:
        >>> compare_volumes(50, 30)
        (50, 'Volume A is greater than Volume B.')
        >>> compare_volumes(100, 100)
        (100, 'Both volumes are equal.')
        >>> compare_volumes(2.5, 4.7)
        (4.7, 'Volume B is greater than Volume A.')

    Note:
        This function does not perform any file I/O or network operations. It relies solely on
        the provided arguments for its logic and output generation.
    """
    
    # Validate input types to ensure we are comparing numbers only
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both inputs must be numeric values (int or float).")

    comparison_message = ""
    
    # Determine the larger value and construct the appropriate message based on logic flow
    if volume_a > volume_b:
        result_value = volume_a
        comparison_message = f"Volume A is greater than Volume B."
    elif volume_b >= volume_a:  # Covers equality or case where B is strictly larger (redundant check for clarity in thought process, but logic holds)
        if volume_a == volume_b:
            result_value = volume_a
            comparison_message = "Both volumes are equal."
        else:
            result_value = volume_b
            comparison_message = f"Volume B is greater than Volume A."

    return (result_value, comparison_message)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    # These represent hypothetical tank capacities in liters and gallons respectively.
    SAMPLE_VOLUME_A: float = 50.0
    SAMPLE_VOLUME_B: int = 30
    
    result_value, status_message = compare_volumes(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)
    
    print(f"Comparison Result:")
    print(f"Larger Volume: {result_value}")
    print(f"Status: {status_message}")