def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive (greater than zero).
    
    Optimized by using a generator expression with early exit as soon 
    a non-positive number is found, rather than iterating through the entire list.
    
    Args:
        numbers (list of int/float): The list to check.
        
    Returns:
        bool: True if all numbers are positive, False otherwise.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    sample_cases = [
        [1, 2, 3],           # Expected: True
        [-1, 2, 3],          # Expected: False
        [],                  # Edge case: Empty list -> True (vacuously true)
        [0.5, -0.5],         # Mixed positive/negative float -> False
        [1.0, 2.0, 3.0]     # Positive floats -> True
    ]

    for i, test_list in enumerate(sample_cases):
        result = check_all_positive(test_list)
        print(f"Test case {i + 1}: Input={test_list}, Output={result}")