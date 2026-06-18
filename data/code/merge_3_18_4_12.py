def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): A non-empty list of numeric values.
        
    Returns:
        bool: True if max(numbers) > numbers[-2], else False.
    """
    if len(numbers) < 2:
        return False
    
    last = numbers[-1]
    second_to_last = numbers[-2]
    
    # Find the maximum value in the list
    max_value = max(numbers)
    
    return max_value > second_to_last

if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 10]
    result = is_max_greater_than_second_to_last(sample_data)
    print(result)  # Expected output: True (max=10 > second-to-last=9)