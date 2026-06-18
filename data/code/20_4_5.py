def equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    if two lists are element-wise equal (assuming same length).
    
    Args:
        list1: First input list.
        list2: Second input list.
        
    Yields:
        True if elements at each index match, False otherwise.
    """
    # Validate lengths first as per problem assumption context
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length.")

    for i in range(len(list1)):
        yield list1[i] == list2[i]

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    # Test Case 1: Identical lists (should yield True)
    a = [1, 'hello', 3.14]
    b = [1, 'hello', 3.14]
    
    result_1 = list(equal_generator(a, b))
    print(f"Test 1 - Equal Lists: {result_1}")

    # Test Case 2: Different lists (should yield False)
    c = [10, 20, 30]
    d = [1, 'hello', 99]
    
    result_2 = list(equal_generator(c, d))
    print(f"Test 2 - Different Lists: {result_2}")

    # Test Case 3: Empty lists (should yield True)
    e = []
    f = []
    
    result_3 = list(equal_generator(e, f))
    print(f"Test 3 - Empty Lists: {result_3}")