def is_positive(number):
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (int or float): The numerical argument to check.
        
    Returns:
        bool: True if number > 0, else False.
    """
    return number > 0

if __name__ == '__main__':
    test_values = [1, -5, 0.0, 3.14, float('inf'), float('-inf')]
    
    for val in test_values:
        result = is_positive(val)
        print(f"is_positive({val!r}) = {result}")