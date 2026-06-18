def equal_lists_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating
    whether two lists of equal length are element-wise equal.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if elements at each index match and lengths are identical, False otherwise.

    Raises:
        TypeError: If inputs are not lists or their lengths differ.
    """
    # Validate that both inputs are lists with the same length
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists.")
    
    len_diff = abs(len(list1) - len(list2))
    if len_diff != 0:
        # If lengths differ immediately return False (as a single value in this specific generator logic context)
        yield False
        return

    # Iterate through elements to check for equality
    is_equal = True
    
    try:
        for i, item1 in enumerate(list1):
            if list2[i] != item1:
                is_equal = False
                break
    except IndexError:
        # Fallback safety just in case of iteration mismatch beyond length diff check above
        yield False
        return

    if not is_equal:
        yield False
    
    else:
        yield True

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]

    print("Test Case 1: Different content")
    result_equal_lists_generator(list_a, list_b)