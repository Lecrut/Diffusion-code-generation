def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using list comprehension which is implemented in C under the hood,
    providing better performance than explicit loops for this simple operation.
    
    Args:
        numbers (list of int): A list of integer values.
        
    Returns:
        list of int: A new list containing only negative integers from input.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample data without user interaction or external dependencies
    sample_data = [-5, -10, 3, -20, 7, -8, -99, 42]
    
    result = filter_negative_numbers(sample_data)
    
    print("Negative numbers:", result)