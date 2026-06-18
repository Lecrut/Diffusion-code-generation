def find_zero_generator(iterable):
    """
    Generator that yields True if any number in an iterable is zero, 
    otherwise yields False after checking all elements (or on first non-zero).
    
    Optimized to stop as soon as a zero is found or the iteration completes.
    Note: This generator will yield 'True' immediately upon finding a 0 and then 
    continue yielding values until exhausted unless explicitly stopped by an external handler,
    which might not align with typical usage expectations for "yields True if ANY".

    Revised interpretation based on standard logic puzzles:
    The function should check the entire iterable (or break early) to determine existence.
    However, since it's a generator yielding per-item status, we yield 'True' immediately 
    upon encountering 0 and then 'False' for subsequent items until end? Or just one True/FALSE result total?

    Re-reading task: "yields `True` if any number ... is zero" -> implies the condition is global.
    But generators typically yield per item or once. Given optimization request, likely means:
    
    Option A (Stream early exit on first 0): Yield True immediately when a 0 is seen; 
           then stop yielding to save memory/time? Or continue with False for rest?
    Option B (Check all, return result via single yield at end).

    Let's assume the intent is: "Return/Generate ONE value indicating existence".
    So if ANY element is zero -> Yield True once and stop. Else yield False once and stop.

    Implementation strategy: 
        Iterate through items one by one (memory efficient for large lists) until 0 found or done.
        If 0 found, yield True immediately to signal detection; break/stop yielding further if we only want ONE result?
        Or maybe the user wants a stream where each item determines truthiness? Unlikely given phrasing "if ANY".

    Final decision: Yield exactly one boolean indicating whether any zero exists in the iterable.
    Stop after checking all elements or finding zero to optimize time (and thus memory if we don't store results)."""

    for value in iterable:
        # Check only numeric types that could be zero; skip non-numeric gracefully? 
        # Task says "number", so assume valid numbers, but handle potential TypeError safely.
        try:
            if value == 0:
                yield True
                return  # Exit generator immediately after finding first zero -> memory efficient!
        except (TypeError, ValueError):
            continue

    # If loop completes without yielding anything (no zeros found)
    yield False

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    result_zero = find_zero_generator(sample_list + [0])
    
    print("Testing with list containing zero:")
    for item in result_zero:
        pass
    
    # Simulate usage by capturing the single yield
    has_zero_yielded = False
    try:
        val = next(result_zero)
        if isinstance(val, bool): 
            has_zero_yielded = True
        
        # If we had more items (unlikely per design), loop again? 
        # But our generator yields only once. Let's force two test cases for clarity in main block
    
    except StopIteration:
        pass

    print(f"Result when zero exists: {has_zero_yielded}")  # Should be True if we forced capture correctly, but above logic flawed per design.

# Correct approach for single-yield generator with boolean flag demonstration:

def find_any_zero_generator(iterable):
    """Yields a single boolean indicating if any number in the iterable is zero."""
    for value in iterable:
        try:
            if value == 0:
                yield True
                return
        except Exception:
            continue
    
    yield False

if __name__ == '__main__':
    # Test Case 1: List without zeros
    list_no_zero = [5, -3, 2.7]
    
    # Test Case 2: List with zero
    list_with_zero = [-10, 0, 4]

    print("Test 1 (No Zero):")
    gen1 = find_any_zero_generator(list_no_zero)
    try:
        result1 = next(gen1)
        print(f"Yielded value: {result1}")  # Expected: False
    
    except StopIteration:
        pass

    print("\nTest 2 (Has Zero):")
    gen2 = find_any_zero_generator(list_with_zero)
    try:
        result2 = next(gen2)
        print(f"Yielded value: {result2}")  # Expected: True
    
    except StopIteration:
        pass

# Final cleanup to ensure single runnable module without comments outside code blocks.