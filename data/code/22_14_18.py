def filter_odds(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Args:
        numbers (list of int): The list of integers to process.
        
    Returns:
        list of int: A list of odd integers found in the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values with various edge cases including negatives, zeros, and evens/odds mix
    sample_list = [-5, -3, -2, -1, 0, 1, 2, 97, 8]
    
    result = filter_odds(sample_list)
    
    print(f"Input: {sample_list}")
    print(f"Filtered odd numbers: {result}")