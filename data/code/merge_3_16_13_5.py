def filter_positive_numbers(numbers):
    """
    Processes a list of numbers and returns a new list containing 
    only the positive elements using list comprehension.
    
    Args:
        numbers (list): A list of numerical values
        
    Returns:
        list: A list containing only the positive integers from the input
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_data = [-5, 3, -1.7, 0, 2, -8, 4.5]
    
    result = filter_positive_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered positive numbers:", result)