def is_max_greater_than_second_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int or float): The input list of numbers.
        
    Returns:
        bool: True if max > second_last, else False.
    """
    if len(numbers) < 2:
        return False
    
    maximum = max(numbers)
    second_to_last = numbers[-2]
    
    return maximum > second_to_last

if __name__ == '__main__':
    sample_list = [3, 7, 1, 9, 4]
    result = is_max_greater_than_second_last(sample_list)
    print(result)  # Expected output: True (max=9, second-to-last=4)