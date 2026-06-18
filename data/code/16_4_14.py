def check_all_positive(numbers):
    """
    Checks if all numbers in a list are positive (> 0).
    
    Args:
        numbers (list of int or float): The list to check.
        
    Returns:
        bool: True if all numbers are strictly greater than zero, False otherwise.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, 2, 3],              # All positive -> Expected: True
        [-1, 2, 3],             # Contains negative -> Expected: False
        [],                     # Empty list (vacuously true all are positive) -> Expected: True
        [0, -5, 10],            # Zero and negatives present -> Expected: False
    ]

    for i, test_list in enumerate(sample_lists):
        result = check_all_positive(test_list)
        expected = "True" if len([x for x in test_list if x <= 0]) == 0 else "False"
        print(f"Test {i + 1}: Input={test_list}, Result={result} (Expected: {expected})")