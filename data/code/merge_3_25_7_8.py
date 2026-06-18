def contains_zero(numbers):
    """
    Checks if zero exists in a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        bool: True if 0 is found, False otherwise.
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, 2, 3],           # Expected: False
        [-5, -1, 0, 4],     # Expected: True
        [],                  # Expected: False (empty list)
        [0.0],               # Expected: True (float zero)
    ]

    for i, test_list in enumerate(sample_lists):
        result = contains_zero(test_list)
        print(f"Test {i + 1}: Input={test_list}, Output={result}")