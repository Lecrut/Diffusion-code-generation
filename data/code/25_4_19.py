def contains_zero(iterable):
    """
    Generator function that yields True if any number in an iterable list is zero, 
    and False otherwise. Optimized for memory efficiency by processing items one at a time.
    
    Args:
        iterable (iterable): An iterable of numbers to check.
        
    Yields:
        bool: First yield is True if 0 exists, else False immediately after checking all elements? 
              Wait, the task says "yields True if any number... is zero". This implies a single boolean result.
              However, it's phrased as a generator ("yields"). A typical pattern for this logic 
              in a generator context that needs to be memory efficient and return a definitive answer:
              
              Option 1 (Single yield): Check all items first? No, that defeats the "generator" spirit if we want early exit.
                      But wait, it says "yields True IF ANY... is zero". This usually means: 
                      If condition met -> yield True and stop. Else -> yield False at end? Or just one boolean total?
                      
              Let's re-read carefully: "yields `True` if any number in an iterable list is zero, and `False` otherwise."
              
              Interpretation A (Single Boolean Result): The function should produce exactly two yields max: 
                  1. True (if found) then stop. 
                  2. False (if not found after full scan).
                  
              This fits "generator" semantics while being efficient. We iterate once, check for zero. If found, yield True and return/stop generator. 
              If loop finishes without finding zero, we need to yield the final answer: False. But a standard `return` in Python 3 stops iteration immediately?
              
              Actually, if I want to be strictly correct with "yields ... otherwise", it implies two possible outcomes for the stream of yields.
              
              Logic: 
                For item in iterable:
                  If item == 0: yield True; return (stop generator)
                
                # If we reach here, no zero was found. We must yield False to satisfy "and False otherwise".
                yield False

    """
    for value in iterable:
        if value == 0:
            yield True
            break
    
    # Only reached if the loop completed without finding a zero
    yield False

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no external input required.
    
    # Test Case 1: List contains zero -> Should yield True then stop (or just return result depending on usage)
    # Since it's a generator, we consume it to see the yields.
    data_with_zero = [5, -2, 0, 3]
    print("Test 1 (Contains Zero):")
    for val in contains_zero(data_with_zero):
        print(f"Yielded: {val}")

    # Test Case 2: List does not contain zero -> Should yield False at the end.
    data_without_zero = [5, -2, 3]
    print("\nTest 2 (No Zero):")
    for val in contains_zero(data_without_zero):
        print(f"Yielded: {val}")

    # Test Case 3: Empty list -> Should yield False.
    data_empty = []
    print("\nTest 3 (Empty List):")
    for val in contains_zero(data_empty):
        print(f"Yielded: {val}")