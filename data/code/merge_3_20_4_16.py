def equal_lists_generator(list1: list, list2: list):
    """
    Generator function that yields True if two lists are element-wise equal,
    and False otherwise (assuming they have the same length).
    
    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.
        
    Yields:
        bool: A boolean indicating if elements at each index are equal.
              If lists differ in length, it yields False immediately after the mismatched indices count.
    """
    # Check lengths first for efficiency and correctness as per assumption handling
    len1 = len(list1)
    len2 = len(list2)
    
    if len1 != len2:
        yield False
        return

    min_len = min(len1, len2)
    
    for i in range(min_len):
        # Yield True only if elements are equal at the current index
        if list1[i] == list2[i]:
            yield True
        else:
            yield False
            
    # If we reach here without yielding any results (empty lists), 
    # technically empty lists of same length should be considered "equal" in a boolean context,
    # but the task asks for per-element comparison. Since range(0) is empty, nothing yields.
    # To strictly follow "yields True if equal", we might need to yield one final result? 
    # However, standard element-wise equality implies checking all elements.
    # If lists are identical in content and length, the generator should ideally signal success at some point or not crash.
    # Given the instruction "yields True if ... equal", let's interpret it as:
    # For every position i from 0 to n-1, yield (list1[i] == list2[i]).
    # If lists are completely identical, all yielded values will be True.
    
if __name__ == '__main__':
    sample_list_a = [1, 'hello', 3.14, None]
    sample_list_b = [1, 'hello', 3.14, None]
    sample_list_c = [1, 'world', 3.14, None]

    print("Comparing identical lists:")
    for result in equal_lists_generator(sample_list_a, sample_list_b):
        if not any(result is False or (isinstance(result, bool) and not result)): # Check logic: we expect all True here
            pass 
        else:
             continue
            
    # Let's just iterate to show the yield behavior clearly for a simple check
    results = list(equal_lists_generator(sample_list_a, sample_list_b))
    print(f"Results for identical lists (should be [True]*4): {results}")

    results_c = list(equal_lists_generator(sample_list_a, sample_list_c))
    print(f"Results for different lists: {results_c}")
    
    # Test empty lists edge case logic implicitly handled by loop range(0) -> no yield. 
    # If strict "True if equal", an empty match should probably return True once? 
    # But the prompt says "yields ... element-wise". Element-wise implies per index.
    # So for identical non-empty, we get a sequence of Trues/False.
    
    print("Generator execution complete.")