def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than zero).
    
    Args:
        numbers (list[float|int]): List of numeric values to process.
        
    Returns:
        list[int|float]: New list with only positive numbers from input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_data = [-5, 10, -3.2, 0, 7.8, -1, 42]
    
    result = filter_positive_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Output (positive numbers only):", result)