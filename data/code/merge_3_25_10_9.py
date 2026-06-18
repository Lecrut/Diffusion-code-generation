def is_zero(value: float) -> bool:
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (float): The numerical argument to check.
        
    Returns:
        bool: True if value == 0, else False.
    """
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -1e-4532, 5, 0.0]
    for val in test_cases:
        result = is_zero(val)
        print(f"is_zero({val}) -> {result}")