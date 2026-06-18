def is_negative(value: float) -> bool:
    """
    Returns True if value is less than zero, False otherwise.
    
    Args:
        value (float): The numerical argument to check.
        
    Returns:
        bool: True if value < 0, else False.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_values = [-5.23, -1, 0, 42.9]

    results = []
    for val in test_values:
        result = is_negative(val)
        results.append(f"is_negative({val}) = {result}")

    # Print all results to the console (no input required)
    print('\n'.join(results))