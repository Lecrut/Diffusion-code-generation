def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than the second-to-last element,
    otherwise returns False. Handles edge cases where there might not be a valid 'second-to-last' element.
    
    Args:
        numbers (list of int or float): A list of numerical values.
        
    Returns:
        bool: True if max(numbers) > second_to_last_element else False.
             If the list has fewer than 2 elements, returns False to indicate no comparison can be made.
    """
    if not numbers or len(numbers) < 2:
        return False
    
    last = numbers[-1]
    second_to_last = numbers[-2]
    
    max_val = max(numbers)
    
    return max_val > second_to_last

if __name__ == '__main__':
    # Sample test cases hard-coded without user input or external dependencies
    sample_data_1 = [5, 3, 8, 9, 2]
    result_1 = is_max_greater_than_second_to_last(sample_data_1)
    
    print(f"Input: {sample_data_1}")
    print(f"Is max ({max(sample_data_1)}) > second-to-last (7)? Result: {result_1}")
    print()
    
    sample_data_2 = [10, 4, 6]
    result_2 = is_max_greater_than_second_to_last(sample_data_2)
    print(f"Input: {sample_data_2}")
    max_val_s2 = max(sample_data_2)
    print(f"Is max ({max_val_s2}) > second-to-last (4)? Result: {result_2}")
    print()
    
    sample_data_3 = [5, 5] # Equal elements
    result_3 = is_max_greater_than_second_to_last(sample_data_3)
    print(f"Input: {sample_data_3}")
    max_val_s3 = max(sample_data_3)
    print(f"Is max ({max_val_s3}) > second-to-last (5)? Result: {result_3}")
    print()
    
    sample_data_4 = [1] # Single element
    result_4 = is_max_greater_than_second_to_last(sample_data_4)
    print(f"Input: {sample_data_4}")
    print("Is max > second-to-last? Result: False (insufficient elements)")