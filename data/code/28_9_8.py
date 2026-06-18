def is_max_greater_than_target(lst, target):
    """
    Recursively determines if the largest element in a list is greater than a target value.
    
    Args:
        lst (list): The input list of numbers.
        target: The value to compare against.
        
    Returns:
        bool: True if the maximum element in the list is greater than target, False otherwise.
    """
    # Base case: empty list or single element
    if len(lst) == 0:
        return False
    
    if len(lst) == 1:
        return lst[0] > target

    # Recursive step: compare current max of sublist with head and tail
    rest_max = is_max_greater_than_target(lst[1:], target)
    
    # If the maximum of the rest is greater than target, we are done.
    if rest_max:
        return True
    
    # Otherwise, check if the first element itself is greater than target
    return lst[0] > target

if __name__ == '__main__':
    sample_list = [5, 3, 8, 2, 9]
    test_target = 7

    result = is_max_greater_than_target(sample_list, test_target)
    
    # Output the result to verify functionality without user input
    print(f"List: {sample_list}")
    print(f"Target: {test_target}")
    print(f"Largest element ({max(sample_list)}) > Target? {result}")