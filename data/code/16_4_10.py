def check_all_positive(numbers):
    """
    Checks if all numbers in a list are positive (greater than zero).
    
    Optimized by using early termination: returns False immediately upon finding 
    any non-positive number, avoiding unnecessary iterations through the rest of the list.
    
    Args:
        numbers (list[float|int]): A list of numeric values to check.
        
    Returns:
        bool: True if all elements are positive (> 0), otherwise False.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    sample_cases = [
        ([1, 2, 3], True),           # All positive -> should be True
        ([-1, -2, -3], False),      # All negative -> should be False
        ([0, 5, 10], False),        # Contains zero -> should be False
        ([1.5, 2.7, 4.9], True),   # Floats all positive -> should be True
        ([-3.5, -1.2], False),      # Negative floats -> should be False
        ([], True),                  # Empty list: vacuously true that "all" are positive
    ]

    for test_input, expected in sample_cases:
        result = check_all_positive(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: Input {test_input} -> Expected {expected}, Got {result}")