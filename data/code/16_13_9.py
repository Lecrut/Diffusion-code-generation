def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list[float|int]): A list of numeric values.
        
    Returns:
        list[float|int]: A list containing only the positive numbers from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 0, 7.2, -1, 99]
    result = filter_positive_numbers(sample_data)
    print(result)