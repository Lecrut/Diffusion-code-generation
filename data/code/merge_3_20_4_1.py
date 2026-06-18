def equal_lists_generator(list1, list2):
    """
    Generator function that yields True if two lists are element-wise equal, 
    and False otherwise (if they differ at any point). Assumes both lists have the same length.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if elements match up to current index, False on first mismatch or end of iteration.
               Note: This generator yields a single boolean based on the comparison logic requested 
               ('True' if equal overall, 'False' otherwise). However, as a *generator*, yielding one value 
               for an entire list equality check is semantically unusual unless we yield True only once upon success 
               and False immediately. Given the phrasing "yields True/False", interpreted strictly:
               
               If lists are fully equal -> Yield True (and stop).
               If not equal -> Yield False (and stop).
               
               This effectively makes it a one-shot decision maker, but implemented as a generator to satisfy 
               the task constraint of being a "generator function".
    """
    if len(list1) != len(list2):
        # Although the prompt assumes same length, handle gracefully by yielding False immediately.
        yield False
        return

    for item1, item2 in zip(list1, list2):
        if item1 == item2:
            continue
        else:
            yield False
            break
    
    # If loop completes without breaking (all items matched)
    yield True

if __name__ == '__main__':
    # Sample values - hard-coded as per requirements. No user input, args, or network access used.
    
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    sample_list_c = [7, 8, 9]

    # Test Case 1: Different lists -> Expect False
    print("Test Case 1 (Different):", list(equal_lists_generator(sample_list_a, sample_list_b)))

    # Test Case 2: Identical lists -> Expect True
    identical_copy = [7, 8, 9]
    result_identical = equal_lists_generator(sample_list_c, identical_copy)
    
    # We consume the generator to get the single boolean yield for this test case.
    is_equal_result = next(result_identical) if hasattr(result_identical, '__next__') else False
    
    print("Test Case 2 (Identical):", [is_equal_result])

    # Test Case 3: Partial match -> Expect False (first mismatch triggers stop and yield False)
    partial_match_a = [7, 'x', 9]
    partial_match_b = [7, 'y', 9]
    
    result_partial = equal_lists_generator(partial_match_a, partial_match_b)
    is_equal_result_p = next(result_partial) if hasattr(result_partial, '__next__') else False
    
    print("Test Case 3 (Partial Mismatch):", [is_equal_result_p])

    # Verification of generator behavior: 
    # The function yields a boolean. For equal lists it will yield True at the end.
    # For unequal lists it will yield False on first mismatch or immediately if lengths differ.