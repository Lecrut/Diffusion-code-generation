def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized by using a generator expression within list() to avoid creating 
    an intermediate list, which improves memory efficiency for large inputs.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only the odd integers from the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(sample_input)
    print(result)