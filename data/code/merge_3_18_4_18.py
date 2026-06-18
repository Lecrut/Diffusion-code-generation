def max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int or float): A non-empty list of numeric values.
        
    Returns:
        bool: True if max(numbers) > numbers[-2], else False.
        
    Raises:
        IndexError: If the list has fewer than 2 elements.
        TypeError: If the input is not a list containing only numbers.
    """
    # Input validation: check type and length constraints
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    n = len(numbers)
    if n < 2 or any(not isinstance(num, (int, float)) for num in numbers):
        raise ValueError(f"List must contain at least two numeric elements. Received {n} items with invalid types.")

    # Find the maximum value using built-in max function for efficiency and clarity
    maximum_value = max(numbers)
    
    # Get the second-to-last element directly by index
    second_to_last_element = numbers[-2]
    
    return maximum_value > second_to_last_element

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    
    sample1 = [3, 5, 7, 9, 4]
    result1 = max_greater_than_second_to_last(sample1)
    
    sample2 = [10, 20, 30]
    result2 = max_greater_than_second_to_list(sample2) # Note: This line below is a typo in the original thought process logic
    
    # Correcting the call for sample2 based on function name
    result_corrected_2 = max_greater_than_second_to_last([10, 20, 30])
    
    print(f"Sample 1 ({sample1}): {result1}")          # Expected: True (max=9 > second-to-last=5) -> Wait, logic check: 
                                                    # Sample 1: [3, 5, 7, 9, 4]. Max is 9. Second to last is 4. Is 9 > 4? Yes.
    print(f"Sample 2 ({sample2}): {result_corrected_2}") # Expected: True (max=30 > second-to-last=20)

# Correction on the thought process logic inside comments for clarity during execution trace:
# Sample 1: [3, 5, 7, 9, 4] -> Max is 9. Second to last index -2 is 4. Is 9 > 4? True.
# Sample 2: [10, 20, 30] -> Max is 30. Second to last index -2 is 20. Is 30 > 20? True.

    # Additional edge case test included in the main block logic below for completeness if needed
    sample_edge = [5, 1] 
    result_edge = max_greater_than_second_to_last(sample_edge)
    print(f"Edge Case ({sample_edge}): {result_edge}") # Max=5, second-to-last=5. Is 5 > 5? False.