def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Parameters:
        numbers (list[int]): List of integers to process.
        
    Returns:
        list[int]: New list with only odd integers preserved in order.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, 9, 6, 7, 0]
    result = filter_odd_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered odd numbers:", result)