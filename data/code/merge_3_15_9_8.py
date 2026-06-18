"""
High-performance algorithm to check if two large lists of elements are identical 
in content and order using early termination on mismatch.

This module implements a direct element-wise comparison optimized for performance.
It avoids unnecessary full list traversals by returning immediately upon finding
a difference at any index, assuming the input lists have equal length.
If lengths differ or an element differs at the same position, it returns False.
Otherwise, if all elements match up to the minimum of both lengths (which should be 
equal for valid inputs), it returns True.

For extremely large datasets where hashing overhead is a concern and order matters,
this O(n) linear scan with early exit provides optimal performance compared to sorting
or set-based approaches which are O(n log n) or require additional memory allocation.
"""

def lists_are_identical(list_a: list, list_b: list) -> bool:
    """
    Check if two lists are identical in content and order.

    Args:
        list_a (list): The first list to compare.
        list_b (list): The second list to compare.

    Returns:
        bool: True if both lists have the same elements in the same order, False otherwise.

    Performance Notes:
        - Time Complexity: O(n) where n is the length of the shorter list. 
          The function terminates immediately upon finding a mismatch or length difference.
        - Space Complexity: O(1), as no additional data structures are created.
    
    Raises:
        TypeError: If either input is not a list.

    Example:
        >>> lists_are_identical([1, 2, 3], [4])
        False
        
        >>> lists_are_identical(['a', 'b'], ['c'])
        False
        
        >>> lists_are_identical([], [])
        True
    
    """
    
    # Validate input types to ensure safety and consistency.
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Both inputs must be Python lists.")

    length_a = len(list_a)
    length_b = len(list_b)

    # Check for length mismatch first as it is an O(1) operation.
    if length_a != length_b:
        return False

    # Perform element-wise comparison with early termination.
    try:
        for i in range(length_a):
            elem_a = list_a[i]
            elem_b = list_b[i]

            # Use identity check (is) first, then equality (=). 
            # This is a micro-optimization; Python's __eq__ handles most cases efficiently.
            if not (elem_a == elem_b):
                return False
        
        # If the loop completes without returning False, lists are identical.
    except IndexError:
        # Should theoretically never be reached due to length check and range() usage,
        # but included for defensive programming in case of internal state corruption.
        return False

    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Test Case 1: Identical lists with integers
    list_1 = [5, 27, 389]
    list_2 = [5, 27, 389]
    result_case_1 = lists_are_identical(list_1, list_2)

    # Test Case 2: Identical strings (case-sensitive order check)
    list_str_a = ["apple", "banana"]
    list_str_b = ["apple", "cherry"]
    result_case_2 = lists_are_identical(list_str_a, list_str_b)

    # Test Case 3: Empty lists
    empty_list = []
    result_case_3 = lists_are_identical(empty_list, empty_list)

    # Test Case 4: Different lengths (should return False early)
    short_list = [1]
    long_list = [0, 1, 2]
    result_case_4 = lists_are_identical(short_list, long_list)

    # Print results to verify functionality.
    print(f"Test Case 1 - Identical integers: {result_case_1}")      # Expected: True
    print(f"Test Case 2 - Different strings at index 1: {result_case_2}") # Expected: False
    print(f"Test Case 3 - Empty lists: {result_case_3}")         # Expected: True
    print(f"Test Case 4 - Different lengths: {result_case_4}")   # Expected: False
    
    assert result_case_1 == True, "Case 1 failed."
    assert result_case_2 == False, "Case 2 failed."
    assert result_case_3 == True, "Case 3 failed."
    assert result_case_4 == False, "Case 4 failed."

    print("All test cases passed successfully.")