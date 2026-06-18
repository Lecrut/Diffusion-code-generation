"""
Module to calculate the ratio of two lengths with error handling.

This module defines a function that computes the ratio of two numeric values,
representing lengths. It includes robust error handling for division by zero.
No interactive input or external dependencies are used in this script.
"""

def calculate_ratio(length_a: float, length_b: float) -> str:
    """
    Calculate and return a formatted string describing the ratio of two lengths.

    Args:
        length_a (float): The first length value (numerator).
        length_b (float): The second length value (denominator).

    Returns:
        str: A message containing either the calculated ratio or an error indication.

    Examples:
        >>> calculate_ratio(10, 5)
        'The ratio of lengths is 2.0.'
        
        >>> calculate_ratio(3, 6)
        'The ratio of lengths is 0.5.'

    Raises:
        ValueError: If the division results in a zero denominator situation 
                   (i.e., length_b is effectively zero after handling floating point epsilon),
                   or if input types are invalid. The function catches this internally 
                   and returns an error string instead to avoid uncaught exceptions,
                   as per graceful error handling requirements for utility functions,
                   but technically raising a ValueError would be more Pythonic for programmatic use;
 however, the task requires handling errors gracefully which implies returning safe output or minimal exception.
 Given "gracefully", we will ensure it never crashes unexpectedly and returns descriptive status.

    Note:
        This function does not interact with stdin, arguments, or external resources.
    """
    # Validate inputs to prevent TypeError
    if not isinstance(length_a, (int, float)) or not isinstance(length_b, (int, float)):
        return "Error: Both length values must be numeric."

    epsilon = 1e-9
    
    # Check for effective zero denominator with a small tolerance for floating point comparisons
    if abs(length_b) < epsilon:
        return f"Error: Division by very small or near-zero value ({length_b}). Cannot compute valid ratio. Please ensure the second length is non-negligible."

    try:
        # Perform calculation safely as division by zero check above handles logic errors; 
        # Python's / operator already raises ValueError if result needs float conversion and operand isn't supported,
        # but standard int/float arithmetic generally requires no manual handling beyond the epsilon check here.
        ratio = length_a / length_b
        
        return f"The ratio of lengths is {ratio}."

    except ZeroDivisionError:
        return "Critical Error: Actual zero division occurred despite checks. Please review inputs for exact zeros."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    SAMPLE_A = 100
    SAMPLE_B = 50
    
    result_message = calculate_ratio(SAMPLE_A, SAMPLE_B)
    
    print(result_message)

    # Test case for division by zero scenario (simulated gracefully via input logic inside the function call below is not allowed directly here, 
    # so we just demonstrate valid output. The internal checks handle it).
    
    # Another sample: A=5, B=10 -> ratio 0.5
    
    SAMPLE_A2 = 5
    SAMPLE_B2 = 3

    result_message_2 = calculate_ratio(SAMPLE_A2, SAMPLE_B2)
    print(result_message_2)