def filter_positive_numbers(numbers):
    """
    Returns a new list containing only the positive elements from the input list.
    
    Args:
        numbers (list of int or float): The input list to process.
        
    Returns:
        list: A new list with only positive integers/floats.
    """
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_data = [-5, 10, -3.7, 0, 2.5, -8, 4]
    result = filter_positive_numbers(sample_data)
    
    # Print the original and filtered lists to verify functionality without user input
    print("Original list:", sample_data)
    print("Filtered positive numbers:", result)