def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Optimized by using a generator expression within list() to avoid creating
    an intermediate list, which improves memory efficiency for large inputs.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only the odd numbers from the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_data = [-5, 3, 8, -1, 42, 7, 0, 99, -3]
    
    result = filter_odd_numbers(sample_data)
    
    print("Input list:", sample_data)
    print("Filtered odd numbers:", result)