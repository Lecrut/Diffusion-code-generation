def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list with only the even numbers preserved in order.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_list = [1, 4, 7, 8, 9, 10, -2, 3, 6]
    result = filter_even_numbers(sample_list)
    print(result)