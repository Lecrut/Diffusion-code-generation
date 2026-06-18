def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the elements that are positive (greater than 0).
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        list: A list containing only the positive integers from the input.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    test_data = [-5, 10, -3.2, 0, 4, 'a', True, False]

    result = filter_positive_numbers(test_data)

    print(f"Input: {test_data}")
    print(f"Positive numbers only: {result}")