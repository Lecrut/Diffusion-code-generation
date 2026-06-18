def is_max_greater_than_target(numbers: list, target) -> bool:
    """
    Recursively determines if the largest element in a list 
    is greater than a specific target value.
    
    Args:
        numbers (list): A list of comparable elements.
        target: The value to compare against.
        
    Returns:
        bool: True if the maximum value in 'numbers' > target, False otherwise.
    """
    # Base case: empty list or single element handling logic integrated below
    if not numbers:
        return False
    
    n = len(numbers)
    
    # Recursive step to find the max recursively (or use first/last for simplicity with recursion depth)
    # To avoid creating a new sub-list every time, we access by index.
    def _find_max_recursive(arr):
        length = len(arr)
        if length == 1:
            return arr[0]
        
        current_val = arr[length - 1]
        remaining_arr = arr[:-1]
        max_of_rest = _find_max_recursive(remaining_arr)
        
        return current_val if current_val > max_of_rest else max_of_rest

    # Find the maximum element in the list using recursion
    largest_element = _find_max_recursive(numbers)
    
    # Compare with target
    return largest_element > target

if __name__ == '__main__':
    sample_list_1 = [3, 5, 2, 9, 7]
    sample_target_1 = 6
    
    sample_list_2 = [10, 4, 2, 8]
    sample_target_2 = 11
    
    result_1 = is_max_greater_than_target(sample_list_1, sample_target_1)
    print(f"List: {sample_list_1}, Target: {sample_target_1}")
    if result_1:
        max_val = _find_max_recursive(sample_list_1) # Helper call to get value for printing
        print(f"Largest element is larger than target. Max was: {max_val}.")
    else:
        print("Largest element is NOT greater than target.")

    result_2 = is_max_greater_than_target(sample_list_2, sample_target_2)
    print(f"List: {sample_list_2}, Target: {sample_target_2}")
    if result_2:
        max_val = _find_max_recursive(sample_list_2) # Helper call to get value for printing
        print(f"Largest element is larger than target. Max was: {max_val}.")
    else:
        print("Largest element is NOT greater than target.")