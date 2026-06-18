def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Uses list comprehension for optimal performance as requested.
    
    Args:
        numbers (list[float|int]): A list of numerical values to filter.
        
    Returns:
        list[float|int]: A list containing only the positive numbers from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample data as per requirements (no user input, files, or network)
    sample_data = [-5, 10, -3.5, 0, 7, -2, 4.89]
    
    result = filter_positive_numbers(sample_data)
    print(result)