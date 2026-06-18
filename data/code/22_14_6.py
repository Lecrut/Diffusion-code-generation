def filter_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to be filtered.
        
    Returns:
        list[int]: A list of odd integers found in the input.
        
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
    
    odd_numbers = filter_odd_numbers(sample_input)
    
    print("Original list:", sample_input)
    print("Filtered odd numbers:", odd_numbers)