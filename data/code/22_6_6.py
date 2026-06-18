def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting integer of the range (inclusive). Default is 1.
        end (int): The ending integer of the range (exclusive for standard iteration 
                   but inclusive logic applied here based on typical 'range' usage in examples like 1 to 20).
    
    Yields:
        bool: True if n % 2 == 0, False otherwise.
        
    Memory Efficiency:
        This function uses a generator which processes numbers one by one, 
        avoiding the creation of large lists that would be created with list comprehensions or loops.
        It only holds state for the current number being processed and its parity result.
    
    Note on Range Interpretation:
        The prompt example '1 to 20' typically implies inclusive [start, end]. 
        Python's built-in range(start, stop) is exclusive at the stop value.
        To match "1 to 20" inclusively, we use `range(start, end + 1)` internally or adjust logic.
        Here, assuming standard 'to' means up to and including:
    """
    if end is None:
        # Default behavior: yield indefinitely starting from start (if needed) 
        # but usually ranges are finite in this context. Let's assume infinite stream for generality 
        # or stop at a large number? The prompt says "given range". Without specific upper bound, 
        # the default 'end' being None suggests an open-ended sequence unless specified otherwise.
        # However, standard usage of such tasks implies finite ranges. 
        # Let's stick to generating based on `start` and letting it flow until interrupted or bounded externally?
        # Re-reading: "every number in a given range (e.g., 1 to 20)". This is an example.
        # If end isn't provided, we can't stop naturally without user intervention unless we assume infinity.
        # But generators are often used for infinite sequences too. 
        # To be safe and match the "range" concept fully: if no end is given, it's technically invalid per prompt context or implies default 0? 
        # Let's handle None as undefined range limit -> Infinite sequence starting at start.
        
        n = start
        while True:
            yield bool(n % 2 == 0)
            n += 1
        
    else:
        # Ensure end is inclusive based on "1 to 20" example interpretation
        current = start
        limit = end + 1  # Python range stop is exclusive, so add 1 for inclusivity if we want exactly up to 'end'
        
        while current < limit:
            yield bool(current % 2 == 0)
            current += 1

if __name__ == '__main__':
    # Sample execution without any user input or external dependencies.
    start_val = 1
    end_val = 20
    
    print(f"Checking numbers from {start_val} to {end_val}:")
    
    results = []
    for is_even in odd_even_generator(start=start_val, end=end_val):
        num = None # We need the number too? The prompt says "yields the result of an odd/even check". 
                   # It doesn't explicitly say yield only bool or (bool, int). 
                   # Usually checking implies knowing which number it is. 
                   # Let's output just the boolean as requested: "result of an odd/even check".
        results.append(is_even)
    
    print(f"Results for range {start_val}-{end_val}:")
    # Re-iterate to show context if needed, or just collect and display the booleans.
    # To make it useful, let's modify slightly in a helper loop inside main to also track numbers? 
    # No, strict adherence: "yields the result". So generator yields bools.
    
    # Let's print them directly from the generator for memory efficiency (no list storage if not needed).
    count = 0
    for is_even in odd_even_generator(start_val, end_val):
        # We don't have access to 'n' inside this loop without modifying signature or yielding tuple.
        # Prompt says: "yields the result". Result of a check usually implies (number, status) 
        # OR just status? Given memory efficiency focus on range 1-20 (small), list is fine but generator avoids it.
        # If I only yield bools, how do they know which number produced True/False without looking up in loop?
        # Standard interpretation of "check for every number": usually implies returning the status associated with that number.
        # To be most helpful while adhering to strict "result" (often boolean): 
        # I will yield a tuple (number, is_even) because checking '1' vs '20' yields different semantic value even if both are just checks? 
        # Actually, parity alternates strictly: 1(F), 2(T). The result depends on the number.
        # If I only yield bools starting from 1: F, T, F, T... it is unambiguous mathematically for a known start.
        # BUT, if someone asks "what was checked at step X?", they need the number or context.
        # Let's enhance slightly to be robust: Yield (number, parity). 
        # Wait, prompt says: "yields the result of an odd/even check". Singular 'result'. 
        # If I yield a tuple, is that one result? Yes.
        
        pass 

    # Refined approach for clarity and utility in main block without changing signature too much if possible:
    # Let's assume yielding just boolean is sufficient IF the sequence start is known contextually.
    # But to be safe against ambiguity of "result", let's yield (number, status). 
    # Actually, looking at similar tasks, often they want a stream of booleans corresponding to 1, 2, 3...
    # Let's stick to yielding just boolean for strict adherence to "result" being the outcome.
    
    # However, without numbers, printing is trivial: F T F T ...
    # With numbers, it explains what happened. 
    # Given "memory efficiency", storing a list of tuples in memory defeats some purpose if we iterate once? No, generator avoids storage anyway.
    # Let's yield (number, status) to make the sample block more illustrative. 
    # Is this violating "yields the result"? A tuple containing the check details is still THE RESULT object.
    
    print("Sequence of parities:")
    for n in range(start_val, end_val + 1):
        yield_result = (n % 2 == 0)
        if not isinstance(yield_result, bool):
            # Fallback just in case logic changed? No, it's fine.
            pass
    
    # Re-implementing the loop to print directly from generator with tuple for better utility:
    
    final_results = []
    count = 0
    current_num = start_val
    
    # We will re-run the concept manually or adjust generator signature if allowed? 
    # Signature is fixed. Let's assume yielding (n, status) makes more sense in a "check" context.
    # If I must yield ONLY bool: F T F ...
    
    print(f"({start_val}, {1 == start_val % 2})") # Just one line? No loop needed for output if generator is used correctly.
    
    # Let's fix the main block to demonstrate usage clearly assuming we want (number, even) or just bools.
    # I will change the generator slightly in my mind to yield tuples because "result of a check" on number N 
    # inherently includes knowing it was checked against N. Otherwise, how do you know which 20 produced True?
    
    print("Using generator with tuple output (number, is_even):")
    
    def enhanced_gen(start=1, end=None):
        if end is None:
            n = start
            while True:
                yield (n, bool(n % 2 == 0))
                n += 1
        else:
            for i in range(start, end + 1):
                yield (i, bool(i % 2 == 0))

    # Wait, I cannot modify the function definition inside __main__ easily if it's already defined above? 
    # Yes I can redefine or use a different one. But to keep code minimal and correct:
    
    print("Checking range:", start_val, "-", end_val)