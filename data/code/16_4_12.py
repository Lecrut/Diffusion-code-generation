def check_all_positive(numbers):
    """
    Checks if all numbers in a list are positive (greater than zero).
    
    Optimized by returning early upon encountering a non-positive number,
    avoiding unnecessary iterations through the entire list when possible.
    
    Args:
        numbers (list of float/int): The list of numbers to check.
        
    Returns:
        bool: True if all numbers are positive, False otherwise.
             If the list is empty or None, returns True by default behavior 
             for "all" checks unless specification implies strictness; 
             following mathematical logic where 'for all x in [], P(x)' is true.
    
    Note: The problem statement defines 'positive' as > 0. Zero and negative numbers make the result False.
    """
    if not isinstance(numbers, list):
        # If input is not a list (though type hint suggests it should be), return True per strict set logic for empty/falsy collection usually meaning condition holds vacuously, 
        # but here we treat non-list as valid to avoid crashing on edge cases while keeping core loop clean.
        try:
            numbers = [numbers] if numbers else []
        except TypeError:
            return len(numbers) == 0
            
    for num in numbers:
        if num <= 0:
            return False
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external input or files.
    
    # Test case 1: All positive integers
    result1 = check_all_positive([1, 2, 3, 4])
    print(f"Test 1 (all positives): {result1}")  # Expected: True
    
    # Test case 2: Mixed including zero and negatives
    result2 = check_all_positive([-5, 0, 1.5])
    print(f"Test 2 (mixed with zero/negative): {result2}")  # Expected: False
    
    # Test case 3: All positive floats
    result3 = check_all_positive([0.0001, 42.5, 99.99])
    print(f"Test 3 (all positives float): {result3}")  # Expected: True
    
    # Test case 4: Empty list (vacuously true)
    result4 = check_all_positive([])
    print(f"Test 4 (empty list): {result4}")  # Expected: True

    # Test case 5: Single positive number
    result5 = check_all_positive([10])
    print(f"Test 5 (single positive): {result5}")  # Expected: True
    
    # Test case 6: List with negative and zero mixed at start
    result6 = check_all_positive([-1, -2.5, -3e-10])
    print(f"Test 6 (all negatives/zero-like float neg): {result6}")  # Expected: False
    
    assert all([isinstance(x, int) or isinstance(x, float) for x in ([1, 2], [-1], [], [4.5])]), "Sample input data structure check."