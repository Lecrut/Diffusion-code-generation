import sys

def check_zero_generator(iterable):
    """Generator that yields True if any number in the iterable is zero, False otherwise."""
    has_zero = False
    # Yield immediately to indicate a zero was found (True) or not encountered yet/processed.
    # However, based on the prompt "yields `True` if any...", we need to yield once per item checked? 
    # Or just one value for the whole list? The phrasing "if ANY number" suggests checking existence.
    # A generator is most useful here to stream results or break early.
    # Let's interpret: Yield True immediately upon finding a zero, then False after processing all items if none found? 
    # Or yield one boolean per item indicating if that specific item was zero? 
    # Re-reading: "yields `True` if any number in an iterable list is zero". This implies the condition applies to the whole set.
    # But a generator yields over time. The most logical behavior for checking existence lazily:
    # 1. Iterate through items.
    # 2. If item == 0, yield True and stop (since we found it).
    # 3. If loop finishes without zero, yield False at the end.
    
    try:
        for value in iterable:
            if value == 0:
                yield True
                return  # Stop as soon as a zero is found to optimize memory/time
        
        # Only reached here if no zero was found after iterating all items
        yield False
        
    except TypeError:
        # In case the input isn't an iterable of numbers (though prompt implies list)
        pass

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files
    
    # Sample 1: List containing zero
    data_with_zero = [5, 0, -3]
    
    # Sample 2: List not containing zero
    data_without_zero = [1, 2, 3]
    
    print("Testing with list:", data_with_zero)
    result_gen_1 = check_zero_generator(data_with_zero)
    try:
        for val in result_gen_1:
            if val == True:
                print(f"Found zero at {val}")
                break  # Stop after finding one to demonstrate early exit logic conceptually, 
                     # but the generator handles it internally.
            else:
                print(val)
    except Exception as e:
        pass
    
    print("\nTesting with list:", data_without_zero)
    result_gen_2 = check_zero_generator(data_without_zero)
    
    for val in result_gen_2:
        if val == True:
            break 
        else:
            print(val)