def get_odd_numbers(numbers):
    """
    Takes a list of integers and returns a new list containing only the odd numbers.
    
    Args:
        numbers (list[int]): A list of integer values to process.
        
    Returns:
        list[int]: A list containing only the odd integers from the input.
        
    Examples:
        >>> get_odd_numbers([1, 2, 3])
        [1, 3]
        >>> get_odd_numbers([])
        []
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or network access
    sample_data = [-5, -3, -1, 0, 1, 2, 4, 7, 9, 10]
    
    result = get_odd_numbers(sample_data)
    
    # Output is not printed to satisfy the "no markdown fences or prose outside code" constraint for non-main blocks,
    # but here we define a variable that could be used. However, since the task asks for runnability and typically 
    # testing implies seeing output in such contexts unless strictly forbidden from print statements (which is not stated),
    # I will assume standard Python module execution allows print for verification within the main block as it's part of the script logic.
    
    # Re-evaluating based on "Return only a single complete runnable Python module" and typical expectations: 
    # Printing to console makes the example verifiable without external inputs.
    
    if result is not None:
        print(f"Input list was {sample_data}")
        print(f"Output odd numbers are: {result}")