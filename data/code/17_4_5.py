def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization: Uses generator expression within list() to avoid creating an intermediate 
    full-sized list if memory is constrained, though for simple filtering this difference is negligible.
    Iterates once through the list (O(n) time complexity).

    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed
    sample_data = [1, 4, 3, 8, 9, 6, 5, 12, 7, 10]
    
    result = filter_even_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Filtered Even Numbers:", result)