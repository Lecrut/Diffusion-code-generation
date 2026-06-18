def is_max_greater_than_second_last(numbers):
    """
    Check if the maximum value in the list is greater than the second-to-last element.
    
    Args:
        numbers (list of int or float): The input list of numbers.
        
    Returns:
        bool: True if max > second_to_last, False otherwise.
              Raises ValueError if the list has fewer than 2 elements.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Find maximum value and its index to handle cases where multiple elements equal max
    max_value = -float('inf')
    max_index = None
    
    for i, num in enumerate(numbers):
        if num > max_value:
            max_value = num
            max_index = i
            
    second_to_last_index = len(numbers) - 2
    second_to_last_value = numbers[second_to_last_index]

    return max_value > second_to_last_value

if __name__ == '__main__':
    # Sample test cases hard-coded without user input or external dependencies
    sample_lists = [
        [1, 5, 3],          # Max is 5 (index 1), second-to-last is 3. True.
        [4, 2, 6, 8],       # Max is 8 (index 3), second-to-last is 6. False? No, max > 6 -> True. Wait: list is [4,2,6,8]. Last=8, 2nd last=6. Max=8. Is 8>6? Yes.
        [-10, -5],          # Max is -5 (index 1), second-to-last is -10. True (-5 > -10).
        [7, 3, 9, 2],       # Max is 9 (index 2), second-to-last is 2. False? No, max=9>2 -> True. Wait: list=[7,3,9,2]. Last=2, 2nd last=9. Max=9. Is 9 > 9? No.
        [10],               # Should raise error (less than 2 elements)
    ]

    for i, test_list in enumerate(sample_lists):
        try:
            result = is_max_greater_than_second_last(test_list)
            print(f"Test case {i + 1}: List={test_list} -> Result: {result}")
            
            # Special handling for the invalid length list to demonstrate error behavior if desired, 
            # but since we need a boolean return generally, let's just skip or catch it.
            # The task asks for a function that returns bool. We'll assume valid input per requirements unless specified otherwise.
        except ValueError as e:
            print(f"Test case {i + 1}: List={test_list} -> Error: {e}")

    # Specific manual run to ensure logic clarity based on the prompt's examples if needed, 
    # but the loop above covers it without user input.