def filter_odd_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list): A list of integers to be filtered.
        
    Returns:
        list: A list of odd integers found in the input. If no odd numbers are 
              present, an empty list is returned. Handles non-integer inputs by 
              ignoring them or raising a TypeError if mixed types cannot be safely 
              handled (though this function assumes all items are intended to be 
              comparable as integers).
    """
    return [num for num in numbers if isinstance(num, int) and not isinstance(num, bool) and num % 2 != 0]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, 0, True, False]
    
    result = filter_odd_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Filtered Odd Numbers:", result)