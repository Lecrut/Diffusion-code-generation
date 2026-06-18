import itertools

def find_matching_pairs(values):
    """
    Generator function that yields True whenever two values in the provided list match,
    iterating over all possible unique pairs using combinations with replacement logic implied by context,
    but strictly following task requirement: yield True only when a match is found between distinct indices.

    Note: The standard interpretation of 'two provided values are found to be a match' implies checking if any two elements at different positions have equal value.
    If the same element cannot pair with itself, we use combinations(range(len(values)), 2).
    """
    
    # Create all unique pairs of indices (i, j) where i != j
    n = len(values)
    for idx1 in range(n):
        for idx2 in range(idx1 + 1, n):
            val1, val2 = values[idx1], values[idx2]
            
            # Check if the two values match (are equal)
            if val1 == val2:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values containing duplicates to test matching logic
    sample_data = [5, 3, 8, 'apple', 5, 'orange']

    print("Matching pairs found:")
    
    # Iterate and collect results (though generator could be used directly)
    matches_found = False
    
    for is_match in find_matching_pairs(sample_data):
        if is_match:
            matches_found = True
            idx1_list = [i + 1 for i, val in enumerate(sample_data)] 
            # We don't actually print indices here as per strict "yield" behavior focus, but this confirms logic works.

    if not matches_found:
        print("No matching pairs found.")