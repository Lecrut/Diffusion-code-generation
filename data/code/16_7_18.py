import math

def is_positive(value):
    """
    Check if a given float value is positive.
    
    This function uses standard comparison operators which handle 
    typical floating-point precision requirements adequately for general use cases.
    It returns True if the number is strictly greater than zero, False otherwise.
    
    Args:
        value (float): The numerical value to check
        
    Returns:
        bool: True if positive, False otherwise
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (1.5, True),           # Clearly positive
        (-3.2, False),         # Negative number
        (0.0, False),          # Zero is not positive
        (math.isinf(42.7) if isinstance(math.inf(float)) else 42.7, math.inf > 0), 
    ]
    
    # Correcting the test case for infinity handling in a simple way
    test_cases = [
        (1.5, True),           # Clearly positive
        (-3.2, False),         # Negative number
        (0.0, False),          # Zero is not positive
        (float('inf'), True),  # Positive infinity
        (float('-inf'), False) # Negative infinity
    ]

    for test_value, expected in test_cases:
        result = is_positive(test_value)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_positive({test_value}) = {result} (expected {expected})")