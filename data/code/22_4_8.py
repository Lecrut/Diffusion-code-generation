def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized using a generator expression within the list constructor, 
    which is generally more memory-efficient than creating an intermediate iterator object.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only odd integers from the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Processing the input list to filter odd numbers
    result = filter_odd_numbers(sample_data)
    
    print(f"Original: {sample_data}")
    print(f"Odds only: {result}")