def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): List of numeric values.
        
    Returns:
        bool: True if max > second_to_last, else False.
    """
    if len(numbers) < 2:
        return False
    
    last_element = numbers[-1]
    second_to_last_element = numbers[-2]
    
    maximum_value = max(numbers)
    
    return maximum_value > second_to_last_element

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 4]
    result = is_max_greater_than_second_to_last(sample_list)
    print(result)  # Expected output: True (max=9, second-to-last=4)