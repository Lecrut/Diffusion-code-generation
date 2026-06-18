"""
Module to compare two length measurements.

This module defines a function that takes two numeric values representing lengths,
calculates their difference (first minus second), and determines which value is greater.
It includes an execution block with hard-coded sample values for testing purposes.

No user input or external dependencies are required.
"""

def compare_lengths(length_a: float, length_b: float) -> tuple[float, str]:
    """
    Compare two length measurements.

    Args:
        length_a (float): The first length measurement.
        length_b (float): The second length measurement.

    Returns:
        tuple[float, str]: A tuple containing the difference (length_a - length_b) 
                          and a string indicating the comparison result ('>', '<', or '=').
    
    Example:
        >>> compare_lengths(10.5, 8.2)
        (2.3, '>')
        >>> compare_lengths(5.0, 5.0)
        (0.0, '=')
    """
    difference = length_a - length_b
    
    if length_a > length_b:
        comparison_result = '>'
    elif length_b > length_a:
        comparison_result = '<'
    else:
        comparison_result = '='

    return float(difference), comparison_result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    SAMPLE_A = 150.75
    SAMPLE_B = 203.4
    
    diff, result_symbol = compare_lengths(SAMPLE_A, SAMPLE_B)
    
    print(f"Comparing {SAMPLE_A} and {SAMPLE_B}")
    print(f"Difference ({SAMPLE_A} - {SAMPLE_B}): {diff}")
    print(f"Comparison Result: {'>' if result_symbol == '>' else '<' if result_symbol == '<' else '='}{result_symbol}")