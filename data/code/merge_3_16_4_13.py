def check_all_positive(numbers):
    """
    Checks if all numbers in a list are positive (> 0).
    
    Optimization: Iterates through the list once, returning False immediately 
    upon encountering any non-positive number (short-circuit evaluation logic),
    rather than checking every element.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        bool: True if all elements are positive, otherwise False.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_1 = [1, 2, 3]
    sample_2 = [-5, 1, 2]
    sample_3 = []
    
    print(f"All positive in {sample_1}? ", check_all_positive(sample_1)) # Expected: True
    print(f"All positive in {sample_2}? ", check_all_positive(sample_2)) # Expected: False
    print(f"All positive in empty list? ", check_all_positive(sample_3)) # Expected: True (vacuously true)