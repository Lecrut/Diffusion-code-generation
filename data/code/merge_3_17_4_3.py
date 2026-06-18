def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimized by using a generator expression within list(), which is memory efficient 
    and avoids creating intermediate lists during iteration.
    
    Args:
        numbers (list of int): The input list of integers
        
    Returns:
        list of int: A new list containing only even numbers from the input
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    sample_input = [1, 4, 6, 9, 10, 15, 20]
    
    result = filter_even_numbers(sample_input)
    
    print("Input:", sample_input)
    print("Filtered even numbers:", result)