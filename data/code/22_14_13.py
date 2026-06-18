def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list of int): A list of integers to process.
        
    Returns:
        list of int: A list containing only the odd integers found in the input.
        
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
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Process the sample data
    odd_numbers = filter_odd_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered odd numbers:", odd_numbers)