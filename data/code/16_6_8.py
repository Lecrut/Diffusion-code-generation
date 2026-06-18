import math

def determine_positivity(num: float) -> bool:
    """
    Determines if a number is positive, negative, or zero.
    
    Args:
        num (float): The numerical value to evaluate.
        
    Returns:
        bool: True if the number is strictly greater than 0, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test cases covering positive, negative, and zero inputs
    test_cases = [
        (5, True),      # Positive integer
        (-3.14, False), # Negative float
        (0, False),     # Zero
        (1e-9, True),   # Very small positive number
        (-1e+9, False), # Very large negative number
    ]

    for input_val, expected_result in test_cases:
        assert determine_positivity(input_val) == expected_result, \
            f"Test failed for input {input_val}: expected {expected_result}, got {determine_positivity(input_val)}"
    
    print("All assertions passed.")