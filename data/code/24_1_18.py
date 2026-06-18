def is_negative(number: float) -> bool:
    """
    Returns True if number < 0, otherwise False.
    
    Args:
        number (float): A numerical value to check.
        
    Returns:
        bool: True if the number is negative, False otherwise.
    """
    return number < 0

if __name__ == '__main__':
    test_cases = [-5.2, -10, -0.001]
    
    for val in test_cases:
        result = is_negative(val)
        print(f"is_negative({val}) -> {result}")
        
    additional_tests = [0, 3.75, float('-inf'), float('inf')]
    for val in additional_tests:
        result = is_negative(val)
        print(f"is_negative({val}) -> {result}")