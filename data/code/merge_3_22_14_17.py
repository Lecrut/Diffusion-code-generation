def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list of int): A list of integers to process.
        
    Returns:
        list of int: A list containing only the odd integers found in the input.
        
    Edge Cases Handled:
        - Empty list returns an empty list.
        - List with no odd numbers returns an empty list.
        - Non-integer elements are ignored (only ints checked for oddness).
    
    Time Complexity: O(n) where n is the length of the input list.
    Space Complexity: O(k) where k is the number of odd integers in the output.
    """
    return [num for num in numbers if isinstance(num, int) and not (num % 2 == 0)]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed
    sample_input = [-5, -3, 0, 1, 2, 7, 8, 9, 10]
    
    result = filter_odd_numbers(sample_input)
    
    print("Input:", sample_input)
    print("Filtered Odd Numbers:", result)