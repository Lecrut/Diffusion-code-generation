def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization: Iterates once through the list using a generator expression,
    which is memory efficient and fast in Python due to deferred evaluation.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only even integers from the input.
    """
    return [n for n in numbers if n % 2 == 0]

if __name__ == '__main__':
    sample_data = [-4, -1, 0, 3, 8, 9, 16, 27]
    
    # Process the hard-coded sample data
    result_even_numbers = filter_even_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Even numbers only:", result_even_numbers)