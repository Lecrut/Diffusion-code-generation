def strictly_increasing_generator(sequence):
    """
    Generator function that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False (or nothing).
    
    Note: The task specifies yielding 'True only when' the condition holds. To maintain 
    a consistent stream corresponding to each element comparison, this implementation 
    yields True for matches and skips non-matches if strict adherence to "yields True ONLY" 
    is interpreted as no output otherwise. However, standard practice for such filters 
    often implies yielding False or None on mismatch. Given the phrasing "yields True only",
    we will yield nothing (skip) when the condition is not met, and True when it is.
    
    If a boolean stream of length N-1 is expected where non-matches are explicitly False:
    This version yields True for matches and does not emit anything else to strictly 
    follow "yields True only". Adjust logic if explicit False output on mismatch was intended.

    Args:
        sequence (iterable): An iterable of comparable values.
    
    Yields:
        bool: True if the current value is greater than the previous one; otherwise, nothing yielded.
    """
    prev = None
    
    for val in sequence:
        # Initialize with a flag to handle the first element correctly (no comparison)
        # The problem implies comparing "current" vs "previous". First element has no previous.
        if prev is not None and val > prev:
            yield True
        
        prev = val

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input, args, network)
    sample_data = [10, 5, 20, 3, 40]

    print("Input sequence:", sample_data)
    
    results = list(strictly_increasing_generator(sample_data))
    
    # Demonstrate the generator output directly in a loop for clarity if needed, 
    # but collecting to list is safer for demonstration without side effects during iteration.
    print("Output (True where strictly increasing):", results)

    # Alternative direct printing style showing exactly what happens step-by-step:
    print("\nStep-by-step trace:")
    prev = None
    count = 0
    for val in sample_data:
        if prev is not None and val > prev:
            result = True
        else:
            # Since we only yield True, this branch produces no output from the generator.
            # We simulate here to show logic flow without changing function behavior.
            continue 
        
        print(f"Value {val} compared to previous {prev}: Yielded True")
        
        if prev is not None and val <= prev:
             print(f"Value {val} compared to previous {prev}: Skipped (not strictly greater)")

    # Re-run the generator logic explicitly for a clean final output block
    gen = strictly_increasing_generator(sample_data)
    while True:
        try:
            item = next(gen)
            if item is not None:  # Ensure we don't print None or garbage
                print(f"Yielded: {item}")
        except StopIteration:
            break
    
    # Final verification list for clarity in the main block output
    final_check = [x for x in strictly_increasing_generator(sample_data)]
    print("Final collected results:", final_check)