def strictly_increasing_generator(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: True if current > previous, else False for all elements >= 2.
              For a single-element or empty sequence, it will yield nothing 
              based on the logic that 'previous' doesn't exist yet. However,
              to match common expectations where every element is checked against its predecessor,
              we assume the first element yields False (no previous). Let's refine:
              
              Actually, let's trace carefully:
              - First item: no previous -> usually considered not strictly increasing relative to prev. 
                But often these tasks imply checking from index 1 onwards or returning a flag per step.
                
              Re-reading the prompt: "yields True only when the current value is strictly greater than the previous"
              
              If sequence = [1, 2, 3]
              i=0 (val=1): no prev -> condition fails? Or undefined? 
                  Standard interpretation: First element cannot be > previous. So yield False or skip?
                  Prompt says "yields True only when...". Implies if not greater, it yields something else?
                  Usually implies a boolean stream aligned with input length.
                  
              Let's assume we iterate through the sequence and compare index i vs i-1.
              For i=0: condition (curr > prev) is technically False because no prev exists to be less than? 
              Or maybe it should just start from the second element?
              
              To be safe and consistent with "current value" having a comparison target, let's yield for every item starting from index 1.
              However, if I must yield something for the first item...
              Let's assume: First item -> yields False (cannot be greater than non-existent previous).
              
    """
    it = iter(sequence)
    
    # Get the first element to initialize 'previous'
    try:
        prev = next(it)
    except StopIteration:
        return
    
    # Yield for every subsequent element in the sequence. 
    # Note: We iterate again from where we left off, but since it's an iterator,
    # we need a loop that processes items one by one including the first? 
    # Actually, let's restructure to process all elements and yield boolean per step.
    
    # Reset approach for clarity on yielding structure matching input length:
    # We will yield False/True based on (current > previous). For index 0, we can't determine strict increase from prev.
    # Let's assume the requirement implies checking pairs or simply that the first yields nothing? 
    # But "yields True only when..." suggests a stream of booleans corresponding to items.
    
    # Refined Logic:
    # Iterate through sequence with index. If i > 0 and seq[i] > seq[i-1], yield True else False.
    
    pass

# Re-implementing cleanly inside the generator logic without external dependencies
def strictly_increasing_generator(sequence):
    items = list(sequence)
    n = len(items)
    
    for i in range(n):
        if i == 0:
            # First element cannot be strictly greater than a non-existent previous.
            yield False 
        elif items[i] > items[i-1]:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    
    print("Input Sequence:", sample_data)
    result_generator = strictly_increasing_generator(sample_data)
    
    results = []
    for val in result_generator:
        results.append(val)
        
    print("Output Flags:", results)

# Test Case with dips to ensure False is yielded correctly when not increasing
sample_dips = [1, 5, 2, 8]
print("\nTest Dipped Sequence:", sample_dips)
result_gen = strictly_increasing_generator(sample_dips)
results_dip = list(result_gen)
print("Output Flags for dipped sequence:", results_dip)

# Expected behavior trace:
# [1]: i=0 -> False (no prev)
# [5]: 5 > 1 -> True
# [2]: 2 < 5 -> False
# [8]: 8 > 2 -> True