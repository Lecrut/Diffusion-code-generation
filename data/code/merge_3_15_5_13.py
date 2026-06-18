def find_matching_pairs(values):
    """
    Generator function that yields True if a match is found between two values,
    iterating over all possible pairs in the provided list.
    
    Args:
        values (list): A list of potential pair elements to check for matches.
        
    Yields:
        bool: True when a matching pair is identified, otherwise does not yield anything 
              on non-matches or after yielding once per unique match type if desired logic applies.
              Based on the task description "yields `True` only when two provided values are found to be a match",
              this implementation yields True for every distinct pair (i, j) where i != j and values[i] == values[j].
    """
    n = len(values)
    # Iterate over all unique pairs of indices (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values containing duplicates to test the generator
    sample_data = [5, 'apple', 3.14, 'banana', 20, 'apple']
    
    print("Checking for matching pairs in:", sample_data)
    
    match_count = sum(1 for _ in find_matching_pairs(sample_data))
    
    # Demonstrate the generator by printing matches found
    results = list(find_matching_pairs(sample_data))
    
    if results:
        print(f"Found {len(results)} matching pair(s).")
        print("Matches detected:", sample_data)
    else:
        print("No matching pairs found.")