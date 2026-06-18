def is_positive(value: float) -> bool:
    """
    Checks if a given float value is positive.
    
    This function performs a standard comparison against zero. 
    While floating-point precision issues can arise in complex calculations,
    for the specific task of determining sign (positive/negative/zero),
    direct comparison with 0.0 is the robust and appropriate method.
    
    Args:
        value (float): The number to check.
        
    Returns:
        bool: True if the value is greater than zero, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (1.5, True),       # Clearly positive
        (-3.2, False),     # Clearly negative
        (0.0, False),      # Zero is not positive
        (1e-10, True),     # Very small positive number
        (-1e-10, False),   # Very small negative number
    ]
    
    for test_value in [test_cases[0][0], test_cases[2][0], -45.6]:
        result = is_positive(test_value)
        print(f"is_positive({test_value}) = {result}")