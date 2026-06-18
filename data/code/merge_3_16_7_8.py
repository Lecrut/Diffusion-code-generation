import sys

def is_positive(value):
    """
    Check if a given float value is positive.
    
    Args:
        value (float): The number to check.
        
    Returns:
        bool: True if the value is strictly greater than zero, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Sample values for testing without user input or arguments
    test_cases = [
        -5.7,       # Negative float
        0.0,        # Zero (not positive)
        42.9168,    # Positive float with decimals
        -3e-5,      # Small negative number in scientific notation
        1E+10,      # Large positive number in scientific notation
    ]

    for num in test_cases:
        result = is_positive(num)
        print(f"Number: {num:.6f} -> Is Positive? {result}")