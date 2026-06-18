"""
Module to compare two length measurements.

This module defines a function that takes two numeric values representing lengths,
calculates their difference (first minus second), and determines which value is greater.
It includes a main execution block with hard-coded sample values for testing purposes.

No user input, command-line arguments, or external dependencies are required.
"""

def compare_lengths(length_a: float, length_b: float) -> tuple[float, str]:
    """
    Compare two length measurements and return the difference and comparison result.

    Args:
        length_a (float): The first length measurement.
        length_b (float): The second length measurement.

    Returns:
        tuple[float, str]: A tuple containing:
            - float: The numerical difference (length_a - length_b).
            - str: A string indicating the relationship ('greater than', 'less than', or 'equal to').
    
    Example:
        >>> compare_lengths(10.5, 7.2)
        (3.3, 'greater than')
    """
    difference = length_a - length_b
    
    if abs(difference) < 1e-9:  # Using a small epsilon for float comparison safety
        result_str = "equal to"
    elif difference > 0:
        result_str = "length_a is greater than length_b"
    else:
        result_str = "length_a is less than length_b"

    return (difference, result_str)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    SAMPLE_A = 10.5
    SAMPLE_B = 7.2
    
    diff, message = compare_lengths(SAMPLE_A, SAMPLE_B)
    
    print(f"Length A: {SAMPLE_A}")
    print(f"Length B: {SAMPLE_B}")
    print(f"Difference (A - B): {diff:.4f}")
    print(f"Comparison Result: {message}")