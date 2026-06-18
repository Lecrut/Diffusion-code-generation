def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to be filtered.
        
    Returns:
        list[int]: A list containing only the odd integers from 'numbers'.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_input = [-5, 3, -1, 8, 7, 0, 9, 4, 6]
    result = filter_odd_numbers(sample_input)
    print(result)