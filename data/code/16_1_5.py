def is_positive(number):
    """
    Returns True if number is strictly greater than zero, False otherwise.
    
    Args:
        number (float|int|numpy.number): A numerical value to evaluate.
        
    Returns:
        bool: Result of the check.
    """
    return isinstance(number, (int, float)) and number > 0

if __name__ == '__main__':
    # Sample tests with hard-coded values
    test_cases = [1, -5, 0.0, 3.14, None]
    
    for case in test_cases:
        try:
            result = is_positive(case) if isinstance(case, (int, float)) else "Invalid input"
            print(f"is_positive({case}) => {result}")
        except TypeError as e:
            # Handle cases like None by printing appropriate message outside the condition
            print(f"is_positive({case}) => Error raised")