"""
Module to check if a float value is positive.
This implementation uses standard comparison operators which handle 
floating-point precision adequately for typical use cases as per the task requirements.
"""

def is_positive(value: float) -> bool:
    """
    Check if the given float value is strictly greater than zero.

    Args:
        value (float): The numerical value to evaluate.

    Returns:
        bool: True if value > 0, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [1.5, -2.3, 0.0, 4e-8, float('-inf'), float('inf')]

    print("Testing is_positive function:")
    for val in test_values:
        result = is_positive(val)
        status = "Positive" if result else "Not Positive (Zero or Negative)"
        print(f"{val}: {status}")