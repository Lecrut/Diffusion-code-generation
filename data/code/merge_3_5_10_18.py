"""
Module to compare two length measurements.

This script defines a function that takes two numeric values representing 
lengths (e.g., in meters, centimeters) and returns both their difference 
and which one is greater or if they are equal.

The module includes an execution block with hard-coded sample values for testing,
ensuring it runs without any user input, command-line arguments, network access,
or external files.
"""

def compare_lengths(value_a: float, value_b: float) -> tuple[float, str]:
    """
    Compare two length measurements and return their difference and comparison result.

    Args:
        value_a (float): The first length measurement to be compared.
        value_b (float): The second length measurement to be compared.

    Returns:
        tuple[float, str]: A tuple containing the numerical difference 
                           between the two values as a float, and a string describing
                           the comparison result ("greater than", "less than", or "equal to").
    
    Examples:
        >>> compare_lengths(10.5, 7.2)
        (3.3, 'value_a is greater than value_b')

        >>> compare_lengths(5.0, 5.0)
        (0.0, 'both values are equal to each other')
    """
    difference = abs(value_a - value_b)

    if value_a > value_b:
        result_message = "value_a is greater than value_b"
    elif value_b > value_a:
        result_message = "value_b is greater than value_a"
    else:
        result_message = "both values are equal to each other"

    return difference, result_message

if __name__ == '__main__':
    # Hard-coded sample values for testing. 
    # No user input or external dependencies required.
    measurement_x: float = 150.25
    measurement_y: float = 87.9
    
    diff_msg_pair = compare_lengths(measurement_x, measurement_y)
    
    print(f"Comparing {measurement_x} and {measurement_y}:")
    print(f"Difference: {diff_msg_pair[0]} meters")
    print(f"Comparison Result: {diff_msg_pair[1]}")

    # Additional test case for equality
    diff_equal = compare_lengths(42.0, 42.0)
    print("\nTest Case (Equality):")
    print(f"Difference: {diff_equal[0]} meters")
    print(f"Comparison Result: {diff_equal[1]}")

    # Additional test case for reverse order to ensure robustness
    diff_rev = compare_lengths(3.14, 2.71)
    print("\nTest Case (Reverse Order):")
    print(f"Difference: {diff_rev[0]} meters")
    print(f"Comparison Result: {diff_rev[1]}")