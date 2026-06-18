def is_max_greater_than_target(numbers: list, target) -> bool:
    """
    Recursively determines if the largest element in a list is greater than a target value.
    
    Args:
        numbers (list): A list of comparable elements.
        target: The threshold value to compare against.
        
    Returns:
        bool: True if the maximum element in 'numbers' is strictly greater than 'target', False otherwise.
    """
    # Base case: If the list has only one element, check it directly.
    if len(numbers) == 1:
        return numbers[0] > target
    
    # Recursive step: Find max of first n-1 elements and compare with nth element (last in slice).
    # We split into [numbers[:-1]] and the last element to maintain recursion on a smaller list.
    sub_max_greater = is_max_greater_than_target(numbers[:-1], target)
    
    if numbers[-1] > target:
        return True
    
    # If neither the max of the rest nor the current last element exceeds the target, then no one does.
    return False

if __name__ == '__main__':
    sample_list = [50, 23, 87, 12, 9]
    test_target = 60
    
    result = is_max_greater_than_target(sample_list, test_target)
    
    # Output the result to verify functionality without user input.
    print(f"Is {max(sample_list)} > {test_target}? Result: {result}")