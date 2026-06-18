def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive.
    
    Args:
        numbers (list): A list of integers or floats to be filtered.
        
    Returns:
        list: A new list containing only the positive values from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, -2, 3.7, 0, 10, -4.2, 8, 0.1]
    
    result = filter_positive_numbers(sample_data)
    print(result)