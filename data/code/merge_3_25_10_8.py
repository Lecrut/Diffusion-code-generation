def is_zero(value):
    """
    Checks if a numerical value is exactly zero.
    
    Args:
        value (float | int): The number to check.
        
    Returns:
        bool: True if the number is exactly 0, False otherwise.
    """
    return abs(float(value)) < 1e-9

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, -0, 0.0, 5, -3.5, float('inf'), float('-inf')]
    
    results = []
    for val in test_cases:
        result = is_zero(val)
        results.append((val, result))

    # Print results to demonstrate functionality without interactive prompts
    print("Testing is_zero function:")
    for val, res in results:
        status = "Zero" if res else "Not Zero"
        print(f"is_zero({repr(val)}) -> {res} ({status})")