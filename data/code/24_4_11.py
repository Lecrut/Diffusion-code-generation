def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized by using a generator expression within a list constructor, which is 
    generally faster than explicit loops in Python due to internal C-level optimizations.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    sample_data = [-5, -10, 3, 7, -2, 0, -8, 42]
    result = filter_negative_numbers(sample_data)
    print(result)