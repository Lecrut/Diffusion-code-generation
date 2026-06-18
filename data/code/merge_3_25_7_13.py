def contains_zero(numbers: list) -> bool:
    """
    Checks if zero exists in the provided list of numbers.
    
    Args:
        numbers (list): A list containing numeric values.
        
    Returns:
        bool: True if 0 is found, False otherwise.
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [1, 2, 3],           # Expected: False
        [-5, 0, 7],          # Expected: True
        [],                  # Expected: False (empty list)
        [0.0, -1.5],        # Expected: True (float zero)
    ]

    for i, test_list in enumerate(sample_lists):
        result = contains_zero(test_list)
        expected = 0 if not any(num == 0 for num in test_list) else 1
        status = "PASS" if int(result) == expected else "FAIL"
        print(f"Test {i + 1}: List={test_list}, Result={result} -> Status: {status}")