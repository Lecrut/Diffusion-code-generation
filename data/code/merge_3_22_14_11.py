def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list with all odd integers from the input.
        
    Raises:
        TypeError: If 'numbers' is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    result = []
    for num in numbers:
        if not isinstance(num, int) or isinstance(num, bool):
            continue  # Skip booleans and non-integers to maintain robustness
        
        if num % 2 != 0:
            result.append(num)
            
    return result

if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Handle potential edge cases by testing with empty list and negative numbers
    test_cases = [
        [],                          # Empty list
        [-5, -4, -3, -2, -1],       # Negative odd/even numbers
        sample_input,               # Standard mixed input
        [0]                         # Zero (even)
    ]

    for i, data in enumerate(test_cases):
        filtered = filter_odd_numbers(data)
        print(f"Test case {i + 1}: Input={data} -> Output={filtered}")