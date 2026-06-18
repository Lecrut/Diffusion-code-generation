def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized by using a generator expression within list() which is memory efficient 
    and faster than explicit loops in Python due to C-level implementation optimizations.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only the negative integers from the input.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    sample_data = [-5, -1, 3, -2.5, 7, -8, 0, -9]
    
    result = filter_negative_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Negative elements only:", result)