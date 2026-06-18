def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        list: A new list with only positive integers/floats from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [-5, 3, -10, 0, 7.5, 2, -3.14, 9]
    
    result = filter_positive_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Output (positive numbers only):", result)