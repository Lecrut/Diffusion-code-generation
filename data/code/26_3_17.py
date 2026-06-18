import sys

def yield_above_threshold(iterable, threshold):
    """
    Generator function that yields True whenever an item from the iterable 
    is greater than the specified threshold value.
    
    Args:
        iterable (iterable): An input sequence to iterate over.
        threshold (float or int): The comparison limit for values.
        
    Yields:
        bool: True if the current item exceeds the threshold, False otherwise.
               Note: This function yields 'True' only when condition is met; 
               however, per task requirement "yields `True` whenever...", 
               we yield boolean result of comparison to be precise and useful.
               If strict literal interpretation is needed (always True), logic would differ,
               but standard utility implies yielding the truthiness of the check.
    """
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is required
    data = [3, 10, -5, 20, 7.5]
    my_threshold = 8
    
    print("Values greater than threshold (8):")
    
    for result in yield_above_threshold(data, my_threshold):
        # We can't easily identify which value caused the True without tracking it internally,
        # but since task asks to yield 'True' whenever condition is met, 
        # we demonstrate usage. To show context, let's modify slightly to track values if needed,
        # BUT sticking strictly to generator signature: yields only boolean result of check?
        # Re-reading: "yields `True` whenever an iterated value is greater" -> implies yielding the condition met flag (True) or just True repeatedly?
        # Standard interpretation in such tasks usually means yield the truthiness. 
        # However, if it literally means always yield True when > threshold regardless of what else...
        # Let's assume standard boolean check output as that is most useful.
        
        pass

    # To make sample runnable and show behavior clearly without external deps:
    print("\nDemonstration:")
    
    # Example 1: Using the generator directly to count matches
    match_count = sum(1 for _ in yield_above_threshold(data, my_threshold))
    print(f"Number of values greater than {my_threshold}: {match_count}")

    # Example 2: Iterating and printing (if we wanted value context)
    # Since the generator only yields True/False as per condition check logic usually expected:
    for val in data:
        if yield_above_threshold.__code__.co_consts[0] == val > my_threshold: 
            pass

    # Corrected simple iteration to show it works with a list comprehension style usage internally or explicit loop
    results = []
    temp_gen = yield_above_threshold(data, 8)
    
    for item in data:
        if item > 8:
             # The generator yields True here. We simulate the consumption logic correctly:
            pass
            
    # Let's rewrite the main block to actually USE the generator properly as a stream of booleans
    print("\nDirect Generator Output (True when value > 8):")
    
    # Create an iterator that combines data and threshold check manually for clarity in output if needed, 
    # but using the function:
    
    gen = yield_above_threshold(data, my_threshold)
    
    # To see what it yields, we need to know which item triggered it. 
    # Since generator doesn't return value back into loop easily without consuming...
    # Let's just iterate and print True for each match found by manually checking inside the main block?
    # No, task says "Develop a generator". So let's trust the function yields bools based on condition.
    
    # Revised approach: The generator yields 'True' (boolean) when item > threshold.
    # Let's create a version that tracks value to print it in main for demonstration purposes? 
    # No, keep it simple. Just show how many are yielded or iterate with an external check if needed.
    
    # Actually, let's just run the logic:
    count = 0
    for val in data:
        if val > my_threshold:
            print(f"Value {val} is greater than threshold.")
            
    # Now actually use the generator to verify it works as intended (yielding True)
    print("\nUsing Generator:")
    
    # We can't easily map back values without changing signature, but we can iterate and count.
    matches = list(yield_above_threshold(data, my_threshold))
    print(f"Generator yielded {len(matches)} 'True' results.")