def find_matching_pairs(values):
    """
    Generator function that yields True if a pair of values from the input list matches,
    otherwise it does not yield anything (or could be structured to indicate non-match).
    
    This implementation iterates over all unique pairs in the provided list.
    If any two elements are equal, it yields 'True' for that match.
    Note: The task asks to yield True only when a match is found. 
    To make the generator useful as an iterator of matches, we will yield (index1, index2) or just iterate until a match is found?
    
    Re-reading the prompt: "yields `True` only when two provided values are found to be a match".
    This implies that if no match exists in the entire list, it should probably not yield anything at all.
    However, standard generator behavior usually expects some output or completion signal. 
    Given the strict phrasing "only when ... found", we will assume:
    1. Iterate through combinations of two items from the list.
    2. If they match (are equal), yield True immediately and stop? Or continue yielding for all matches?
    
    Usually, in such logic puzzles, if it says "yields true only when ... found", 
    it might imply finding *the* first match or listing all matches. 
    Let's assume we want to find at least one pair of matching values (duplicates).
    If duplicates exist, yield True for each duplicate pair encountered? Or just once per unique value that has duplicates?
    
    To be safe and robust: We will iterate through the list using indices i < j. 
    If values[i] == values[j], we yield 'True'. 
    Since it says "only when ... found", if no match is ever found, nothing should be yielded.
    """
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the two values are a match (equal)
            if values[i] == values[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values containing duplicates to test the generator.
    # Example: [10, 20, 30, 40, 50, 60, 70] -> No matches expected (yields nothing).
    # We will use a list with repeated numbers like [1, 'a', 2, 'b', 1].
    
    sample_data = [1, 'apple', 3.14, 'banana', 5, 'cherry', 6]
    
    print("Scanning for matching pairs in:", sample_data)
    matches_found = False
    
    # Consume the generator to check if any True is yielded
    result_list = list(find_matching_pairs(sample_data))
    
    if not result_list:
        print("No matching values found.")
    else:
        print(f"Found {len(result_list)} match(es).")