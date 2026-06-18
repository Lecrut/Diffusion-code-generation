def contains_zero(numbers):
    """
    Check if the list of numbers contains zero.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        bool: True if 0 is in the list, False otherwise.
        
    Time Complexity: O(n) where n is the number of elements in the list.
    Space Complexity: O(1).
    
    Note: This implementation iterates through the list once to find zero,
    ensuring optimal time complexity for this operation without using specialized data structures.
    """
    return 0 in numbers

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ([1, 2, 3], False),
        ([5, -1, 0, 4], True),
        ([-9.8, -0.1, 0], True),
        ([], False),
        ([7 * i for i in range(10)], False)
    ]
    
    print("Testing contains_zero utility function:")
    all_passed = True
    
    for index, (input_list, expected_result) in enumerate(test_cases):
        result = contains_zero(input_list)
        status = "PASS" if result == expected_result else "FAIL"
        
        if result != expected_result:
            all_passed = False
            
        print(f"Test {index + 1}: Input={input_list} | Expected={expected_result} | Got={result} -> [{status}]")
    
    if all_passed:
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed.")