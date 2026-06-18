def find_matching_pairs(values):
    """
    Generator function that yields True if any pair of values in the input list matches,
    otherwise it does not yield anything (or could be modified to yield False on no match).
    
    This implementation checks all unique pairs from the provided list. If a matching 
    pair is found where both elements are identical and distinct indices exist, it yields True immediately upon finding one such case.
    However, based on typical generator patterns for "finding matches", this version will yield False if no match exists after checking all combinations.
    
    Note: The requirement states to yield `True` only when a match is found. 
    To make the function useful as a boolean indicator without yielding True multiple times or indefinitely,
    we can structure it to check pairs and return/yield appropriately at the end if no matches are found after iteration.
    
    Since generators cannot easily "return" a single value like `False` unless they yield nothing (which implies False in some contexts) 
    or explicitly yield False once all checks complete without success, we will design it to:
    - Iterate through unique pairs of indices.
    - If values[i] == values[j], yield True immediately and stop further yielding for this run? 
      But generators don't have a 'stop' flag other than breaking the loop internally via return or raising StopIteration.
      
    Revised approach per strict generator semantics:
    We'll iterate through all pairs, collect matches in memory first (since we need to know if ANY match exists), then yield True once at the end? 
    But that breaks pure generator flow for "yield only when". 
    
    Actually, re-reading: "yields `True` only when two provided values are found to be a match"
    This implies multiple yields of True could occur if there are multiple matching pairs.
    
    Let's implement it as checking every pair and yielding True whenever a match is detected between distinct indices.
    If no matches exist, the generator simply finishes without yielding anything (which effectively acts like False in boolean context)."""

    seen_pairs = set()  # To avoid redundant checks for symmetric pairs if needed, though not strictly necessary
    
    n = len(values)
    
    # Iterate over all unique pairs of indices (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                yield True

if __name__ == '__main':
    sample_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Add duplicate values to ensure at least one match exists for demonstration
    modified_sample = sample_values + [sample_values[0]] 
    
    print("Checking pairs in:", modified_sample)
    
    has_match = False
    
    # Create a generator and consume it
    matches_found = list(find_matching_pairs(modified_sample))
    
    if not matches_found:
        result_value = "No matching pair found"
    else:
        result_value = f"Matching pairs detected (yielded {len(matches_found)} True values)"
        
    print(result_value)

if __name__ == '__main__':
    pass
