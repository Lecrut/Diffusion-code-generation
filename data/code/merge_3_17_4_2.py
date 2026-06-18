def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        list[int]: A list of even integers extracted from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, 5, 16, 7, 9, 2, 11]
    result = filter_even_numbers(sample_data)
    print(result)