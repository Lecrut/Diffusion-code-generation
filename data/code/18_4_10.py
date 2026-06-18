def has_max_greater_than_second_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): The input list of numbers.
        
    Returns:
        bool: True or False based on the comparison condition.
    """
    if len(numbers) < 2:
        return False
    
    max_value = max(numbers)
    second_last_index = -2 if len(numbers) >= 3 else -1
    # For lists of length 2, second-to-last is index 0 (the first element). 
    # Wait, "second-to-last" means the one before the last.
    # If list has 2 elements [a, b], last is b(1), second-to-last is a(0).
    # So general formula for index of second-to-last in 0-indexed list: len - 2
    
    if numbers[-1] == max_value and (len(numbers) < 3 or numbers[-2] >= max_value):
        return False
        
    return True

# Correction to logic above based on standard definition:
def has_max_greater_than_second_last_v2(numbers):
    """
    Returns True if the maximum value in the list is strictly greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): The input list of numbers.
        
    Returns:
        bool: True or False based on the comparison condition.
    """
    if len(numbers) < 2:
        return False
    
    max_value = max(numbers)
    second_last_element = numbers[-2]
    
    # Check if maximum is strictly greater than the second-to-last element
    return max_value > second_last_element

if __name__ == '__main__':
    sample_data_1 = [3, 5, 7, 9]
    result_1 = has_max_greater_than_second_last_v2(sample_data_1)
    
    # Test case: Max is 9. Second to last is 7. 9 > 7 -> True
    print(f"Test Case 1 (Input: {sample_data_1}): Maximum ({max(sample_data_1)}) vs Second-to-last ({sample_data_1[-2]})")
    
    sample_data_2 = [5, 3, 4, 6]
    result_2 = has_max_greater_than_second_last_v2(sample_data_2)
    
    # Test case: Max is 6. Second to last is 4. 6 > 4 -> True
    
    print(f"Test Case 1 (Input: {sample_data_2}): Maximum ({max(sample_data_2)}) vs Second-to-last ({sample_data_2[-2]})")
    
    sample_data_3 = [10, 5, 8, 6]
    result_3 = has_max_greater_than_second_last_v2(sample_data_3)
    
    # Test case: Max is 10. Second to last is 6. 10 > 6 -> True
    
    print(f"Test Case 3 (Input: {sample_data_3}): Maximum ({max(sample_data_3)}) vs Second-to-last ({sample_data_3[-2]})")
    
    sample_data_4 = [7, 9, 5, 8]
    result_4 = has_max_greater_than_second_last_v2(sample_data_4)
    
    # Test case: Max is 9. Second to last is 5. 9 > 5 -> True
    
    print(f"Test Case 4 (Input: {sample_data_4}): Maximum ({max(sample_data_4)}) vs Second-to-last ({sample_data_4[-2]})")