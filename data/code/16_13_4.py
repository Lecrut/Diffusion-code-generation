def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list[int|float]): List of numerical values.
        
    Returns:
        list[int|float]: A new list with only positive integers or floats.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-3, -1, 0, 2, 4.5, 7, None, "string", 8.9]
    
    # Filter the positive numbers from the hard-coded sample data
    result = filter_positive_numbers(sample_data)
    
    print("Filtered list:", result)