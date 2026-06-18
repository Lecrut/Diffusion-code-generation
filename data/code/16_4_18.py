def check_all_positive(numbers):
    """
    Returns True if all numbers in the list are positive, otherwise False.
    Optimized to return early on first non-positive value found.
    
    Args:
        numbers (list of int or float): The list of numerical values to check.
        
    Returns:
        bool: True if every number is strictly greater than zero, else False.
    """
    for num in numbers:
        if not (num > 0):
            return False
    return True

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    sample_1 = [1, 2, 3]
    result_1 = check_all_positive(sample_1)

    sample_2 = [-1, 5, 0.5]
    result_2 = check_all_positive(sample_2)

    sample_3 = []
    result_3 = check_all_positive(sample_3)

    print(f"All positive in {sample_1}: {result_1}")       # Expected: True
    print(f"Has negatives/zeros in {sample_2}: {not result_2}")  # Expected: True (so all not pos is True, but function returns False for the list itself) -> Function returns False. Logic check: sample_2 has -1 and 0.5. One is negative/zero? No zero here but one neg. So not positive. Result should be False. The print line asks "Has negatives/zeros", which implies it expects a true if there are issues. My function checks if *all* are positive. If any fail, returns False.
    # Correction on sample_2 logic for the output statement: 
    # check_all_positive([-1, 5, 0.5]) -> -1 is not > 0 -> Returns False immediately.
    
    print(f"All positive in empty list {sample_3}: {result_3}")       # Expected: True (vacuous truth)

    assert result_1 == True
    assert result_2 == False
    assert result_3 == True
    
    print("All tests passed.")