"""
Module to calculate the ratio of two lengths with error handling.

This module defines a function that computes the ratio of one length divided by another,
handling potential division by zero errors gracefully. It includes a main execution block
with hard-coded sample values for testing purposes without requiring any user input or external dependencies.
"""

def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculate the ratio of two lengths (length_a / length_b).

    Args:
        length_a (float): The numerator length value.
        length_b (float): The denominator length value.

    Returns:
        float or None: The calculated ratio if successful, otherwise None in case of division by zero.

    Raises:
        No exceptions are raised; errors are handled internally and returned as None.
    
    Examples:
        >>> calculate_length_ratio(10.0, 2.0)
        5.0
        >>> calculate_length_ratio(5.0, 0.0)
        None
    """
    if length_b == 0:
        return None
    
    ratio = length_a / length_b
    return ratio

if __name__ == '__main__':
    # Sample values for testing without user input or command-line arguments
    sample_length_numerator = 15.0
    sample_length_denominator = 3.0

    result_normal_case = calculate_length_ratio(sample_length_numerator, sample_length_denominator)
    
    if result_normal_case is not None:
        print(f"Ratio of {sample_length_numerator} to {sample_length_denominator}: {result_normal_case}")
    else:
        print("Error in calculation.")

    # Test case for division by zero
    test_division_by_zero = calculate_length_ratio(10.0, 0.0)
    
    if test_division_by_zero is None:
        print(f"Handled gracefully for {10.0} / {0.0}: Division by zero detected.")