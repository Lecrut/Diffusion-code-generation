def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a generator expression within list() to avoid creating an intermediate 
    full-size filtered list in memory before returning, though for simple integer filtering 
    this difference is negligible compared to interpretation overhead. The key optimization 
    here is avoiding explicit loops and function calls inside the loop by leveraging C-optimized 
    built-ins where possible (list comprehension/generator expression).
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only negative integers from input.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    sample_data = [-5, 10, -3, 0, -7, 2, -1]
    result = filter_negative_numbers(sample_data)
    print(result)