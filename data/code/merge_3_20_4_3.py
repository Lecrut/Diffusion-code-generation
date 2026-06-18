def element_wise_equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields True if two lists are element-wise equal,
    and False otherwise, assuming they have the same length.
    
    Since a generator can only yield one value before being exhausted,
    this implementation checks equality immediately upon receiving both inputs
    (as generators cannot peek ahead to see all elements without consuming them).
    However, adhering strictly to the "generator" requirement while yielding
    exactly once: we iterate through the lists in parallel. If any pair of 
    corresponding elements differ, or if lengths mismatch during iteration,
    False is yielded immediately and the generator stops (implicitly by raising StopIteration).
    
    Note: True generators must yield at least one value to be considered "yielding".
    The logic here yields a single boolean result based on full comparison.
    """
    # Check length first as per assumption, but handle mismatch gracefully inside loop if needed.
    len1 = len(list1)
    len2 = len(list2)
    
    iterator1 = iter(list1)
    iterator2 = iter(list2)
    
    try:
        while True:
            item1 = next(iterator1)
            item2 = next(iterator2)
            
            if item1 != item2:
                yield False
                return  # Stop after finding a difference
            
            # If loop completes without returning, lists are equal.
            # To strictly follow "yields True", we need to signal success at the end.
    except StopIteration:
        pass
    
    if len1 == len2 and not any(item1 != item2 for _ in list1): 
        # Re-evaluating logic because a pure generator checking full equality without consuming all first is tricky.
        # A true solution that yields exactly once at the end after processing requires knowing it's done.
        yield True

    return False

# Corrected implementation focusing on yielding exactly one value based on complete comparison:
def element_wise_equal_generator_v2(list1, list2):
    """
    Generator function that yields a single boolean result indicating if two lists are equal.
    It processes the elements and decides whether to yield True or False at completion.
    Since generators can't easily "return" without yielding last in Python 3 unless using return (which raises StopIteration),
    we use `yield` for success/failure explicitly. If no difference found, it yields True; otherwise False immediately.
    
    However, the prompt asks to yield 'True' if equal and 'False' otherwise. 
    A generator that exits without yielding anything is often not useful. 
    We will ensure exactly one value is yielded: either at the first mismatch (yielding False) or after full traversal (yielding True).
    
    To make it a proper generator for comparison, we can iterate and yield status on-the-fly? 
    But "yields True if ... equal" implies a single result. Let's assume single boolean output is expected from the generator object itself upon completion/exhaustion logic or immediate exit.
    
    Refined approach: Iterate once. If mismatch found -> yield False, raise StopIteration immediately (simulating end). 
    If loop finishes without return statement inside try-except block that yields True? 
    Actually, standard idiom for "yield result" is just to let the function finish and use `return` if allowed or explicit yield at end.
    
    Let's implement a version that iterates fully in memory (since lists are passed) but behaves as a generator yielding once:
    """
    # We assume input lists have same length per task description, 
    # but we handle the comparison logic inside an iterator loop to look like a stream processing.
    
    try:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                yield False
                return  # Exit generator immediately on first mismatch
        
        # If we reach here, all elements were equal. 
        # We must yield True to satisfy the requirement of yielding a value when they are equal.
        yield True
    except IndexError:
        # This block should theoretically not be reached if lengths match and loop range is correct,
        # but acts as safety net for length mismatch detection during iteration logic if needed elsewhere.
        pass

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]

    result_generator = element_wise_equal_generator_v2(sample_list_a, sample_list_b)
    
    # Consume the generator to get the single boolean value
    is_equal_result = next(result_generator) if hasattr(next(result_generator), '__iter__') else False
    
    try:
        val1 = next(result_generator)
    except StopIteration:
        pass
        
    print(f"Lists are equal: {val1}")

# Wait, the above logic for consuming was flawed. Let's rewrite cleanly to ensure exactly one yield happens correctly.