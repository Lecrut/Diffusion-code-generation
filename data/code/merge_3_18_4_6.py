def is_max_greater_than_second_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.
    
    Args:
        numbers (list of numeric types): The input list of numbers.
        
    Returns:
        bool: True if max(numbers) > numbers[-2], else False.
        
    Note: Assumes the list has at least 2 elements as per logical requirements 
         for accessing second-to-last element. If less than 2, returns False.
    """
    # Ensure the list is not empty and has at least two elements
    if len(numbers) < 2:
        return False
    
    maximum = max(numbers)
    
    # Second to last element index calculation (len - 2)
    second_last_index = len(numbers) - 2
    
    # Compare maximum with the value at second_to_last position
    return maximum > numbers[second_last_index]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ([1, 5, 3], True),           # Max (5) > second last (1) -> True
        ([20, 19, 47, 68], False),   # Max (68) == last, but check against sec_last(19)? Wait: 
                                     # List is [20, 19, 47, 68]. Max=68. Second to last = 47.
                                     # Is 68 > 47? Yes -> Should be True (Corrected below)
        ([5], False),                # Less than 2 elements -> False
    ]

    # Re-evaluating test case [20, 19, 47, 68]:
    # Max is 68. Second to last index is len-2 = 4-2=2 => value at index 2 is 47.
    # Condition: Is max (68) > second_last (47)? Yes -> Expected True in code logic above.

    corrected_tests = [
        ([1, 5, 3], True),           # Max(5) > SecLast(1) -> True
        ([20, 19, 47, 68], True),   # Max(68) > SecLast(47) -> True (Original logic held but sample description was vague)
                                    # Actually let's make a clear False case: [50, 40] where max=50, sec_last=40? 
                                    # Wait, if list is [30, 10], Max=30, SecLast=None/Invalid. Return False anyway due to length check.
        ([7, 8], True),              # Max(8) > SecLast(7) -> True (Wait max should be 8? No max of [7,8] is 8). 
                                   # If list is [50, 10], Max=50, SecLast=10. 50>10 -> True.
        ([3, 2, 4, 1], False),       # Let's craft a case: List=[9, 8]. Max=9, SecLast=8? No wait...
                                   # If I want FALSE: Need max == second_last or list logic issue.
                                   # Actually simply [5, 3] -> Max=5 > 3 (True). 
                                   # How about a list where all elements are equal? [4, 4]. Max=4, SecLast=4. 4>4 is False.
    ]

    final_tests = [
        ([10, 2], True),             # Max(10) > 2 -> True
        ([5, 3], True),              # Max(5) > 3 -> True
        ([7, 8], True),              # Wait max is 8. SecLast is 7. 8>7->True. 
                                   # Let's make a specific False example: [2, 2] or where elements are equal? No wait...
                                   # If I want FALSE result from condition > : Max == Second Last.
        ([50], True),                # Length < 2 -> False (Handled in function)
    ]

    # Let's re-verify logic for [7, 8]: 
    # numbers = [7, 8]
    # max(numbers) = 8
    # second_last_index = len - 2 = 0 => value is 7.
    # Is 8 > 7? Yes -> True.

    # Let's create a case that returns False: 
    # List where Max equals Second Last (since condition is strictly greater).
    test_false_case = [5, 5]   # Max=5, SecLast=5 => 5>5 is False.
    
    sample_input_list = [30, 20, 40, 10] 
    # For this list: 
    # List indices: 0->30, 1->20, 2->40, 3->10
    # Max is 40. Second last index (len-2=2) -> value is 40.
    # Is max(40) > sec_last(40)? No -> False.

    run_test_list = sample_input_list
    
    result = is_max_greater_than_second_last(run_test_list)

    print(f"Input: {run_test_list}")
    print(f"Maximum value in list: {max(run_test_list)}")
    print(f"Second-to-last element: {run_test_list[-2]}")
    print(f"Is Maximum > Second-to-last? {result}")