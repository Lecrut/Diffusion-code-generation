def find_matching_pairs(values):
    """
    Generator function that yields True if a pair of values from the input list matches,
    otherwise it does not yield anything (or could be modified to yield False based on specific needs).
    
    In this implementation:
    - We iterate through all unique pairs in the provided list.
    - If any two elements are equal, we yield True exactly once per match found.
    
    Parameters:
        values (list): A list of potential pair candidates.
        
    Yields:
        bool: True if a matching pair is found; otherwise nothing for that iteration step.
    """
    seen_pairs = set()  # To avoid duplicate yieldings of the same match
    
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                pair_key = (min(values[i], values[j]), max(values[i], values[j]))
                if pair_key not in seen_pairs:
                    yield True
                    seen_pairs.add(pair_key)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies.
    sample_data = [1, 2, 3, 4, 5]

    print("Testing generator with:", sample_data)
    
    results = list(find_matching_pairs(sample_data))
    
    if not results:
        print("No matching pairs found in the provided data.")
    else:
        print(f"Found {len(results)} matching pair(s).")