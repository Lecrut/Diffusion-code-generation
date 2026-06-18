def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to be filtered.
        
    Returns:
        list[int]: A list of odd integers found in the input list.
        
    Raises:
        TypeError: If 'numbers' is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    result = []
    for num in numbers:
        if not isinstance(num, int) or isinstance(num, bool):
            continue  # Skip booleans and non-integers
        
        if num % 2 != 0:
            result.append(num)
            
    return result

if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    filtered_output = filter_odd_numbers(sample_input)
    
    print("Input:", sample_input)
    print("Filtered Odd Numbers:", filtered_output)