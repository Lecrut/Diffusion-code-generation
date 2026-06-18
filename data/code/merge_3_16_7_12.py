import sys

def is_positive(value):
    """
    Check if a given float value is strictly positive (greater than zero).
    
    While floating-point precision issues exist in arithmetic operations, 
    direct comparison of constants usually suffices as per the task requirements.
    This function checks if value > 0 directly.

    Args:
        value (float): The numerical value to check.

    Returns:
        bool: True if value is positive, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed
    test_cases = [1.5, -2.3, 0.0, float('inf'), float('-inf')]

    for num in test_cases:
        result = is_positive(num)
        print(f"Is {num} positive? {result}")