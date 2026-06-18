def is_max_greater_than_second_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int or float): List of numerical values.
        
    Returns:
        bool: Boolean indicating whether max > second_last.
    """
    if len(numbers) < 2:
        return False
    
    last_element = numbers[-1]
    second_last_element = numbers[-2]
    
    maximum_value = max(numbers)
    
    return maximum_value > second_last_element

if __name__ == '__main__':
    sample_list_1 = [3, 5, 7, 9, 4]
    sample_list_2 = [10, 10, 10]
    sample_list_3 = [5, 8, 6, 9]
    
    print(f"List {sample_list_1}: {is_max_greater_than_second_last(sample_list_1)}")
    print(f"List {sample_list_2}: {is_max_greater_than_second_last(sample_list_2)}")
    print(f"List {sample_list_3}: {is_max_greater_than_second_last(sample_list_3)}")