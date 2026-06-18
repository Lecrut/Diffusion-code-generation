def element_wise_equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    if two lists are element-wise equal (assuming they have the same length).
    
    Args:
        list1: First input list.
        list2: Second input list.
        
    Yields:
        True if elements at each index match, False otherwise.
    """
    # Check lengths first as per assumption requirement handling
    if len(list1) != len(list2):
        yield False
        return
    
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            continue
        else:
            yield False
            break  # Once a mismatch is found, we can stop yielding (or just exit loop)
    
    # If the loop completes without breaking, all elements matched
    yield True

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test Case 1: Equal lists -> Should yield True
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    
    result_equal = []