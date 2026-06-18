def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of int/float): List of numerical values.
        
    Returns:
        bool: True if max > second_to_last, else False.
    """
    if len(numbers) < 2:
        return False
    
    last = numbers[-1]
    second_to_last = numbers[-2]
    
    maximum = max(numbers)
    
    return maximum > second_to_last

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    sample_list_1 = [3, 5, 7, 9, 8]
    result_1 = is_max_greater_than_second_to_last(sample_list_1)
    
    sample_list_2 = [10, 5, 6, 4, 10]
    result_2 = is_max_greater_than_second_to_last(sample_list_2)
    
    sample_list_3 = [1, 2, 3]
    result_3 = is_max_greater_than_second_to_last(sample_list_3)

    print(f"Test 1 ({sample_list_1}): {result_1}")  # Expected: True (7 > 4? No -> False. Wait max=9>6=True)
    
    # Correction on comment above logic for sample_list_1: 
    # Max is 9, second to last is 8 (index -2). 9 > 8 is True.
    
    print(f"Test 2 ({sample_list_2}): {result_2}")  # Expected: False (Max=10 == 4? No wait, max is 10. Second to last index -2 of [5,6,4,10] is 6. So check if list indices matter or value positions)
    pass
    
    print(f"Test 3 ({sample_list_3}): {result_3}")  # Expected: True (Max=3 > second_to_last(2)? Yes -> False? Wait logic again.)

    # Re-verifying the function definition against samples to ensure correct output based on problem statement
    def verify_logic(numbers):
        last = numbers[-1]
        if len(numbers) >= 4: 
            print(f"List {numbers}: Last={last}, SecondToLast={numbers[-2]}, Max={max(numbers)}, Result={is_max_greater_than_second_to_last(numbers)}")

    # Hardcoded final execution block for clarity and simplicity