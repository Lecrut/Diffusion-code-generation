def find_occurrences(text: str, target: str) -> list[tuple[int, int]]:
    """
    Finds all starting and ending indices of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        target (str): The substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains the start and end indices 
                              of an occurrence. If not found, returns an empty list.
                              
    Note: End index is exclusive in Python slicing convention (matching str.find behavior).
          Overlapping occurrences are detected if they exist at different positions.
          However, once a match ends, search continues from the character after it to avoid 
          re-indexing the same characters unless specified otherwise for overlapping matches.
    """
    results = []
    
    # Handle edge cases where target is empty or longer than text
    if not target:
        return [0]  # Returning a list with just index 0 as per typical convention, but 
                  # strictly based on task "find occurrences", an empty string matches everywhere.
                  # However, to match standard `str.find` logic and keep it robust for general use:
    if not target or len(text) < len(target):
        return results

    start_index = 0
    
    while True:
        pos = text.find(target, start_index)
        
        if pos == -1:
            break
        
        # Record the match (start is inclusive, end is exclusive for consistency with Python slicing)
        end_index = pos + len(target)
        results.append((pos, end_index))
        
        # Move to the next character after the current occurrence to handle overlapping 
        # potential correctly without re-matching same characters. 
        # If strict non-overlapping was desired per-segment, we would jump by full length here anyway.
        start_index = pos + 1

    return results

if __name__ == '__main__':
    sample_text = "ababa"
    sample_target = "aba"
    
    indices_list = find_occurrences(sample_text, sample_target)
    
    print(f"Searching for '{sample_target}' in: {repr(sample_text)}")
    if not indices_list:
        print("No occurrences found.")
    else:
        print("Occurrences (start, end):", indices_list)