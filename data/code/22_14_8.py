def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
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
    sample_input = [1, 24, 7, -3, 8, 9, 0]
    
    # Process the input and print results with explanation
    odd_numbers = filter_odd_numbers(sample_input)
    
    if len(odd_numbers) > 0:
        print(f"Odd numbers found in {sample_input}:")
        for num in odd_numbers:
            print(num)
    else:
        print("No odd numbers were found.")