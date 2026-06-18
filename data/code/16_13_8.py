def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive.
    
    Args:
        numbers (list[float]): List of numerical values to process.
        
    Returns:
        list[float]: New list with only positive numbers.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, -2, 3, 0, 7, -10, 4.5]
    result = filter_positive_numbers(sample_data)
    print(result)