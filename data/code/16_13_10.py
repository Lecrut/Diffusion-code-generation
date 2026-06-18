def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing only positive elements.
    
    Parameters:
        numbers (list[float|int]): A list of numeric values to process.
        
    Returns:
        list[int|float]: A list of positive integers or floats from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, 10, -3.7, 0, 2.5, -8, 9]
    result = filter_positive_numbers(sample_data)
    print(result)