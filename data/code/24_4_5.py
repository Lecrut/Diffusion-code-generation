def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a generator expression within a list constructor to avoid 
    creating intermediate lists and minimize memory overhead during iteration.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_data = [-5, -10, 3, -7, 20, -1, 42, -89]
    
    result = filter_negative_numbers(sample_data)
    
    # Output the result for verification purposes only (no interactive prompts used)
    print(result)