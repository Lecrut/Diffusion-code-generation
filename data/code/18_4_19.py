def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): The input list of numbers.
        
    Returns:
        bool: True if max > second_to_last, else False.
    """
    if len(numbers) < 2:
        return False
    
    last_element = numbers[-1]
    second_to_last = numbers[-2]
    
    maximum_value = max(numbers)
    
    return maximum_value > second_to_last

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_lists = [
        [5, 3, 8],          # Max is 8, second-to-last is 3 -> True
        [10, 20, 15],       # Max is 20, second-to-last is 10 -> False (wait: max > second_to_last? No)
    ]

    for i, numbers in enumerate(sample_lists):
        result = is_max_greater_than_second_to_last(numbers)
        print(f"List {i+1}: {numbers} => Result: {result}")

    # Additional manual verification logic for clarity if needed later
    test_list_1 = [5, 3, 8]
    max_val_1 = max(test_list_1)
    second_last_1 = test_list_1[-2]
    
    print(f"\nManual check for {test_list_1}:")
    print(f"Max: {max_val_1}, Second-to-last: {second_last_1}")
    print(f"Is max > second-to-last? {max_val_1 > second_last_1}")