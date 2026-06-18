def find_matching_pairs(values):
    """
    Generator function that yields True if a matching pair is found in the list,
    otherwise it does not yield anything (or could be modified to indicate no match).
    
    This implementation iterates through all possible unique pairs of values.
    If both elements in a pair are equal, it yields True for that specific iteration step.
    """
    n = len(values)
    # Iterate over indices i and j where 0 <= i < j < n to ensure distinct positions
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values containing duplicate elements to trigger matches
    sample_data = [3, 5, 2, 8, 9, 5, 10, 3, 7]
    
    print("Scanning for matching pairs...")
    
    match_count = 0
    
    # Convert generator to list to easily count and iterate if needed, 
    # though the task asks for a generator. We will consume it directly here.
    matches_found = find_matching_pairs(sample_data)
    
    results = []
    for is_match in matches_found:
        if is_match:
            match_count += 1
    
    print(f"Total matching pairs found: {match_count}")