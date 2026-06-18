def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list): A list of numerical values to process.
        
    Returns:
        list: A new list with only positive integers or floats from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_data = [-5, 3, -12, 0, 7.5, -8, 4]
    
    result = filter_positive_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered positive numbers:", result)