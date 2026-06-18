"""
Module to compare two length measurements.

This module defines a function that takes two numeric values representing lengths,
calculates their difference (absolute value), and determines which is greater or if they are equal.
It includes a main execution block with hard-coded sample values for testing purposes.

No user input, command-line arguments, network access, or file I/O is required.
"""

def compare_lengths(value_a: float, value_b: float) -> tuple[float, str]:
    """
    Compare two length measurements and return the difference and comparison result.

    Args:
        value_a (float): The first length measurement.
        value_b (float): The second length measurement.

    Returns:
        tuple[float, str]: A tuple containing:
            - float: The absolute difference between the two values.
            - str: A string indicating the relationship ('greater than', 'less than', or 'equal to').
    """
    diff = abs(value_a - value_b)

    if value_a > value_b:
        result_str = "value_a is greater than"
    elif value_b > value_a:
        result_str = "value_b is greater than"
    else:
        result_str = "equal to"

    return diff, f"{result_str} {value_b}" if value_a > value_b else (f"{result_str} {value_a}",)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    length_1 = 50.75
    length_2 = 48.3

    difference, comparison_message = compare_lengths(length_1, length_2)

    print(f"Comparison of {length_1} and {length_2}:")
    print(f"Difference: {difference}")
    print(f"Result: {comparison_message[0]} {comparison_message[1] if isinstance(comparison_message, tuple) else ''}")