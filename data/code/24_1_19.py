def is_negative(number: float) -> bool:
    """
    Returns True if number is less than zero, False otherwise.
    
    Args:
        number (float): The numerical argument to evaluate.
        
    Returns:
        bool: True if number < 0, else False.
    """
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [-5.0, -1, 0, 3.14]
    
    results = []
    for val in test_cases:
        result = is_negative(val)
        results.append(f"is_negative({val}) -> {result}")
    
    print("\n".join(results))