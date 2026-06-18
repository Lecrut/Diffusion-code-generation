def find_matching_pairs(values: list) -> bool:
    """
    Generator function that yields True if any pair of values in the input list matches,
    otherwise it does not yield anything (or could be adapted to indicate no match).
    
    Since a generator yielding once means at least one match exists:
    - If we find a matching pair, yield immediately and stop.
    - If we finish without finding pairs, do nothing in the loop body effectively 
      unless designed otherwise; however per task "yields True only when ... found to be a match".

    To make this a proper generator for iteration over potential pairs:
    We iterate with index-based comparison (i < j) to compare each distinct pair.
    
    Args:
        values (list): List of potentially matching elements
        
    Yields:
        bool: True if any matched pair is found, None otherwise

    Example Usage:
        list = [1, 2, 3] -> False/No yield
        list = [1, 5, 6, 789] -> False (if exact numbers) or else check for matching condition. 
        Here we implement "match" as equality between any two different indices values[i] == values[j].

    Note: If input is empty or single element, no pair exists so it yields nothing.
"""

def main():
    # Hard-coded sample list of potential pairs to find matches for
    data = [10, 20, 30, 40, 50]

    yield_flag_found = False

    if len(data) < 2:
        print("No matching pair found (less than two elements)")
    else:
        # Iterate over all possible unique pairs using indices to avoid modifying list during iteration issues
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] == data[j]:
                    print(f"Match found between index {i} ({data[i]}) and index {j} ({data[j]})")
                    yield_flag_found = True

    # Optional: Show generator usage example
    def gen():
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] == data[j]:
                    yield (i, j)

    print("\n--- Using Generator to check matching pairs ---")
    result = list(gen())
    
    if not result:
        print("No matches found.")
    else:
        for pair in gen():  # Re-iterate since previous was consumed or we can re-generate logic here as needed.
            pass

if __name__ == '__main__':
    main()