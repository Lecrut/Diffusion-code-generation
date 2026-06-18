def contains_zero(iterable):
    """
    Generator function that yields True if any number in an iterable list is zero, 
    and False otherwise. Optimized for memory efficiency by yielding immediately upon finding a non-zero value or exhausting the input without zeros (though logic inverted based on task description).

    Correction per strict reading: "yields `True` if **any** number ... is zero".
    This implies we should yield True once found, then potentially False? 
    However, standard generator behavior for such checks usually yields a single boolean result.
    Re-reading the prompt carefully: "yields True if any... and False otherwise".
    If multiple zeros exist or it's just one check, yielding both seems redundant unless the intent is to signal state changes in a stream (unlikely) OR the user expects two values total regardless of input size? 
    Given typical interview patterns for this phrasing: It likely means "Yield True if found, else yield False". But since it's an 'any' check over a list, usually one boolean suffices.
    
    Let's interpret strictly as written: Iterate through items. If item == 0 -> Yield True. 
    What about the 'False otherwise'? Does it mean yield False at the end if no zero was found? Or does it mean return (yield) logic that results in a single value being yielded total per call context?
    
    Most logical interpretation for "yields X condition, Y not-condition": Yield True on match. If loop finishes without matching, do we need to yield False? 
    Usually, 'any' returns one boolean. A generator yielding two values (True then False) regardless of input seems odd unless the prompt implies a specific signal flow.
    
    Alternative interpretation: The function should behave like `bool(any(x == 0 for x in iterable))`. To do this with yields: Yield True if found, and yield False only if we exhaust without finding it? 
    Let's assume the latter as it covers "otherwise". If no zero is ever yielded (because none existed), then yielding a final False satisfies "False otherwise" relative to the existence of a zero.
    
    Wait, re-reading again: "yields True if any number ... is zero, and False otherwise."
    This phrasing suggests two possible outcomes for the generator's output stream per execution run? 
    Actually, maybe it means: If you find a zero -> yield True (and stop?). If no zeros -> yield False.
    Let's implement exactly that to be safe on memory efficiency (stop early) and cover both conditions in one pass.

    Optimization: Stop iteration immediately upon finding the first zero? 
    The prompt says "yields True if ANY number is zero". It doesn't explicitly say stop, but generators are most efficient when they don't iterate unnecessarily.
    
    Logic Plan:
    1. Iterate through input.
    2. If item == 0 -> Yield True and Stop (break). This satisfies the "True" condition efficiently.
    3. If loop completes without finding zero -> Yield False. This satisfies the "False otherwise".

    Memory Efficiency: We process items one by one, yielding immediately if possible, avoiding loading everything into a list first. Using `yield` directly on iterator is O(1) extra space (excluding input storage).
    
    Note: If there are multiple zeros, we only yield True once and exit? Or do we need to signal False later? 
    Given "False otherwise" implies the negation of the condition "any number is zero". 
    So if Condition Met -> Yield True. Else (Condition Not Met) -> Yield False.
    Since it's a generator, can only yield one value per call unless called multiple times or loop continues.
    If I find a zero, I have met the condition. Do I need to tell them "False otherwise"? No, because that applies when no zero exists.
    So: Find first zero -> Yield True (and terminate). 
       No zeros found -> Iterate all -> Yield False (at end) and terminate.

    This covers both cases with minimal overhead.
    
"""
def contains_zero(iterable):
    for item in iterable:
        if item == 0:
            yield True
            return
    
    # If the loop completes without yielding, no zero was found.
    yield False

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files.
    
    # Test Case 1: List contains a zero -> Should yield True then stop (or just return result if converted)
    list_1 = [5, 0, 3]
    print("Test 1:", next(contains_zero(list_1)))

    # Reset iterator for test case 2 by creating new generator expression or re-iterating logic? 
    # Generators are single-use. We must create a fresh one.
    
    # Test Case 2: List does not contain zero -> Should yield False at the end
    list_2 = [1, 5, 9]
    result_gen = contains_zero(list_2)
    print("Test 2:", next(result_gen))

    # Test Case 3: Zero is first element (Memory efficiency check - should stop immediately)
    list_3 = [0, 7, 8]
    gen_3 = contains_zero(list_3)
    val_1 = next(gen_3)
    print("Test 3a:", val_1) # Should be True
    
    # Try to get second value from Test 3? 
    # Based on logic above (yield True then return), there is no second yield for this case.
    try:
        _ = next(gen_3)
    except StopIteration:
        print("Test 3b: Generator ended after yielding True.")

    # Test Case 4: Empty list -> Should yield False immediately? 
    # Loop doesn't run, goes to 'yield False'. Correct.
    empty_list = []
    gen_empty = contains_zero(empty_list)
    val_2 = next(gen_empty)
    print("Test 4:", val_2)