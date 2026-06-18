def is_max_greater_than_target(numbers: list, target) -> bool:
    """
    Recursively determines if the largest element in 'numbers' 
    is greater than 'target'.
    
    Args:
        numbers (list): A non-empty list of comparable elements.
        target: The value to compare against the maximum.
        
    Returns:
        bool: True if max(numbers) > target, False otherwise.
    """
    # Base case: single element list
    if len(numbers) == 1:
        return numbers[0] > target
    
    # Recursive step: find max of rest and compare current head with it
    # We assume the function correctly identifies that there is a larger 
    # element in the tail than the head, or vice versa.
    
    if len(numbers) == 1:
        return numbers[0] > target
    
    first = numbers[0]
    rest = numbers[1:]
    
    max_of_rest = find_max_recursive(rest)[0]
    
    # Determine overall maximum by comparing head and max of tail
    current_max = first if first >= max_of_rest else max_of_rest
    
    return current_max > target

def find_max_recursive(numbers):
    """Helper to recursively find the actual maximum value in a list."""
    if len(numbers) == 1:
        return numbers[0]
    
    rest_max = find_max_recursive(numbers[1:])
    first_val = numbers[0]
    
    # Return (value, index) logic isn't needed here as we just need the max value for comparison.
    # However, to strictly follow recursion without helper state complexity:
    return max(first_val, rest_max)

def is_largest_greater_than(numbers, target):
    """
    Main recursive function wrapper that finds the largest element 
    and checks if it exceeds the target using a single pass logic structure.
    
    This implementation uses an auxiliary stack-like recursion to track 
    the maximum found so far from right to left or simply compares recursively.
    To keep it purely functional as requested: we find max via helper, then compare.
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    # Helper to get max value using recursion (internal logic)
    def _get_max_recursive(lst):
        n = len(lst)
        if n == 1:
            return lst[0]
        
        rest_max = _get_max_recursive(lst[1:])
        head_val = lst[0]
        
        # Compare current head with the max of the remaining elements
        return head_val if head_val > rest_max else rest_max

    largest_value = _get_max_recursive(numbers)
    
    return largest_value > target

if __name__ == '__main__':
    sample_list_1 = [3, 7, 2, 9, 5]
    target_1 = 6
    
    # Test case 1: Max is 9, which is greater than 6. Expected True.
    result_1 = is_largest_greater_than(sample_list_1, target_1)
    
    sample_list_2 = [3, 7, 2, 4, 5]
    target_2 = 8
    
    # Test case 2: Max is 7, which is not greater than 8. Expected False.
    result_2 = is_largest_greater_than(sample_list_2, target_2)

    sample_list_3 = [10]
    target_3 = 5
    
    # Test case 3: Single element list where max (10) > 5. Expected True.
    result_3 = is_largest_greater_than(sample_list_3, target_3)

    print(f"Test 1 ({sample_list_1} vs {target_1}): {'True' if result_1 else 'False'}")
    print(f"Test 2 ({sample_list_2} vs {target_2}): {'True' if result_2 else 'False'}")
    print(f"Test 3 ({sample_list_3} vs {target_3}): {'True' if result_3 else 'False'}")

    # Verification logic to ensure correctness based on expected outcomes
    assert result_1 == True, "Largest (9) should be greater than target (6)"
    assert result_2 == False, "Largest (7) should not be greater than target (8)"
    assert result_3 == True, "Max (10) should be greater than target (5)"

    print("All tests passed.")