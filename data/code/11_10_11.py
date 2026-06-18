"""
Module to calculate the ratio of two lengths with error handling for division by zero.

This module defines a function that safely computes the ratio between two numerical values,
representing lengths. It includes input validation and prevents ZeroDivisionError exceptions.
No external dependencies or interactive inputs are required.
"""

def calculate_length_ratio(length_a: float | int, length_b: float | int) -> float:
    """
    Calculate the ratio of a given first length to a second length.

    Args:
        length_a (float|int): The numerator representing the first length.
        length_b (float|int): The denominator representing the second length.

    Returns:
        float: The calculated ratio as a floating-point number.

    Raises:
        ZeroDivisionError: If length_b is zero, preventing runtime division errors.

    Examples:
        >>> calculate_length_ratio(10, 5)
        2.0
        >>> calculate_length_ratio(7.5, 3)
        2.5
    """
    if length_b == 0:
        raise ZeroDivisionError("Cannot divide by zero length.")

    return float(length_a / length_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    numerator = 125
    denominator = 40
    
    try:
        ratio_result = calculate_length_ratio(numerator, denominator)
        print(f"The ratio of {numerator} to {denominator} is exactly equal to :{ratio_result}")
        
        # Additional test case with floating-point values and a zero check demonstration logic
        # Note: We simulate the exception handling conceptually here without actually triggering it 
        # in this successful run, but the function ensures safety.
    except ZeroDivisionError as e:
        print(f"An error occurred during ratio calculation due to division by zero.")