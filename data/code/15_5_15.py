def find_matching_pairs(values):
    """
    Generator function that yields True if two values in the list match each other,
    otherwise it does not yield anything (or implicitly yields False via lack of action 
    but per strict 'yields only when' logic, we assume yielding a boolean flag).
    
    Interpretation: Iterate over all unique pairs. If pair[i] == pair[j], yield True.
    Otherwise do nothing for that iteration to strictly follow "only when... found".
    However, standard generator patterns often expect an output per comparison or just the matches.
    Given "yields True only when...", we will iterate and yield True on match.
    
    Note: To ensure every comparison is processed logically in a testable way 
    (though strictly not yielding False), let's assume the user might want to know 
    if no pairs were found or just list them.
    
    Re-reading prompt: "yields `True` only when two provided values are found to be a match".
    This implies we should iterate through indices i and j, check equality, and yield True on success.
    """
    n = len(values)
    # Iterate over all pairs (i, j) where i < j to avoid duplicates and self-matches unless specified otherwise
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values containing a duplicate pair (3 and 'apple')
    test_data = [5, "hello", 3, "world", 3, "apple"] 
    
    results = list(find_matching_pairs(test_data))
    
    print("Matching pairs found:", len(results))
    for is_match in results:
        if is_match:
            # Identify which values matched by re-scanning or logic during generation
            pass 
    # To demonstrate the yield behavior clearly, we can reconstruct what was yielded.
    # Since the generator doesn't store state easily without wrapping, let's just print the count of matches found.
    
    # Let's create a small wrapper to show actual pairs for clarity in this module context
    def find_and_show_pairs(data):
        seen_indices = {} 
        for i, val in enumerate(data):
            if val in seen_indices:
                prev_idx = seen_indices[val]
                print(f"Match found at indices {prev_idx} and {i}: both are '{val}'")
                yield True
            else:
                seen_indices[val] = i
    
    matches_found_count = sum(find_matching_pairs(test_data))
    print(f"\nTotal number of matching pairs yielded: {matches_found_count}")