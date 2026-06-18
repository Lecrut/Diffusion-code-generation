def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list): A list of numerical values to process.
        
    Returns:
        list: A new list with only the positive integers from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, 3, -1, 0, 2, -7, 8, -2, 4]
    result = filter_positive_numbers(sample_data)
    print(f"Input: {sample_data}")
    print(f"Output (positive numbers only): {result}")