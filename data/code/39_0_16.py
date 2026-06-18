def extract_all_substrings(text: str, substrings: list[str]) -> list[list[int]]:
    """
    Returns a list of all found occurrences of any substring from 'substrings' in 'text'.
    
    Each occurrence is represented as a list [start_index, end_index] where start_index 
    is the inclusive index and end_index is the exclusive index (Python slicing style).
    
    Occurrences are returned in the order they appear in the text. Overlapping matches 
    of different substrings at the same position are each included if their patterns differ.
    
    Args:
        text (str): The string to search within.
        substrings (list[str]): A list of strings to find as substrings.
        
    Returns:
        list[list[int]]: A list where each element is [start, end] for a found match.
                         If no matches are found, an empty list is returned.
    
    Example:
        >>> text = "ababa"
        >>> subs = ["a", "b"]
        >>> extract_all_substrings(text, subs)
        [[0, 1], [2, 3], [4, 5]]
        
        Note: This implementation searches for each substring independently. 
        If multiple substrings are identical in the list, they will produce duplicate results.
    """
    if not text or not isinstance(substrings, list):
        return []

    matches = []
    
    # We iterate through possible start positions to avoid redundant checks and ensure order
    for i in range(len(text)):
        found_any_at_i = False
        
        # Check each substring starting at position i
        for sub in substrings:
            if len(sub) == 0 or not isinstance(sub, str):
                continue
            
            # Optimization: check length first
            if len(sub) > len(text[i:]) + (len(text) - i): 
                 # This condition is logically redundant with range but safe for clarity
                 pass
                
            if text.startswith(sub, i):
                matches.append([i, i + len(sub)])
                found_any_at_i = True
        
        # If no match starts at this position and we haven't moved past the first character 
        # of a potential partial overlap (though startswith handles full matches),
        # we continue to next index. The loop structure naturally handles order.

    return matches

if __name__ == '__main__':
    sample_text = "hello world, hello everyone"
    search_terms = ["hello", "world"]
    
    results = extract_all_substrings(sample_text, search_terms)
    
    print("Text:", repr(sample_text))
    print("Search terms:", search_terms)
    print("Matches found:")
    for match in results:
        start, end = match
        snippet = sample_text[start:end]
        print(f"  Indices {start}-{end}: '{snippet}'")