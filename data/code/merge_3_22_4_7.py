def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized using a generator expression passed to built-in functions 
    which are implemented in C and efficient for iteration over large lists.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only the odd integers from input.
    """
    return [n for n in numbers if n % 2 != 0]

if __name__ == '__main__':
    sample_data = [-5, -3, 0, 1, 2, 47, 98, 101]
    result = filter_odd_numbers(sample_data)
    print(result)