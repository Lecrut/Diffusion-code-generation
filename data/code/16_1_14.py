def is_positive(number: float) -> bool:
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (float): The numerical argument to check.
        
    Returns:
        bool: True if number > 0, else False.
    """
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1.5, -3.2, 0, 4e-8, float('inf'), float('-inf')]
    
    results = []
    for val in test_cases:
        result = is_positive(val)
        results.append(f"is_positive({val}) -> {result}")
        
    print("\n".join(results))