def find_matching_pairs(values):
    """
    Generator function that yields True if a pair of values from the list matches,
    otherwise it does not yield anything (or could be designed to skip).
    
    This implementation iterates through all unique pairs in the provided list.
    If any two elements are equal, it yields 'True' exactly once for each such match found.

    Args:
        values (list): A list of potential pair candidates.

    Yields:
        bool: True if a matching pair is found within the list context.
    
    Note: This generator logic assumes we need to detect existence or specific pairing 
          based on equality. Since standard Python generators yield items one by one,
          and "yielding only when two values match" implies detecting pairs, this function
          will iterate through indices (i, j) where i < j. If values[i] == values[j], it yields True immediately
          upon finding the first matching pair to satisfy the condition of yielding 'only' under a specific 
          interpretation of "found". However, if multiple matches exist and we must yield for each match found:
          
    Revised Interpretation based on strict reading ("yields True only when..."):
    Usually implies an event trigger. Let's implement it such that it yields True every time a new matching pair is discovered.

    """
    
    n = len(values)
    # Iterate through all unique pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample list containing duplicate elements to trigger the match condition.
    # Example: [5, 'a', 3, 'b', 5, 'c'] -> Pairs (0,4) are both 5.
    data = [10, 20, 30, 10, 40]

    results = list(find_matching_pairs(data))

    # Output the results to verify functionality without external input or files.
    if not results:
        print("No matching pairs found.")
    else:
        print(f"Found {len(results)} matching pair(s).")