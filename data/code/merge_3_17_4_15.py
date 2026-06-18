def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 6, 8, -2, 9, 15, 32]
    result = filter_even_numbers(sample_data)
    print(result)