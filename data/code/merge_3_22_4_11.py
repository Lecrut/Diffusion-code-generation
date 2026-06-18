def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Optimized using a generator expression passed to built-in 'filter' and 
    converted to a list, which is generally efficient in Python for this operation
    as it avoids creating intermediate lists during iteration.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only the odd integers from 'numbers'.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies.
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = filter_odd_numbers(sample_data)
    
    # Output the result for verification purposes in a simple print statement.
    print(result)