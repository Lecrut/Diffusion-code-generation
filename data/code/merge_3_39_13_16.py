def extract_substrings(text: str, start_points: list[int], end_points: list[int]) -> list[str]:
    """Extract all substrings from text that fall between specified (start, end) index pairs."""
    # Validate inputs ensure lengths match and indices are within bounds before processing.
    if len(start_points) != len(end_points):
        raise ValueError("Start and end points lists must have the same length.")
    
    results = []
    
    for i in range(len(text)):
        is_in_range = False
        
        # Check current index against all defined ranges to determine inclusion.
        for s, e in zip(start_points, end_points):
            if s <= i < e:
                is_in_range = True
            
            # If the character was previously part of a range and now isn't (or vice versa), it marks boundary points? 
            # Actually, the task asks for substrings "between" specified start/end.
            # A simpler interpretation often used in such abstract problems without specific context:
            # Is there a single contiguous block defined by min(starts) to max(ends)? Or is it about finding text segments 
            # that match a pattern? 
            # Re-reading the prompt strictly: "extract all substrings ... that fall between specified start and end points".
            
    # Let's refine based on standard interpretation of such tasks when context like "between brackets" isn't given explicitly as regex.
    # If multiple disjoint intervals are provided (e.g., indices [2,5] and [8,10]), the user likely wants substrings within these windows? 
    # Or does it mean extract text from index min(start) to max(end)?
    # Given "all substrings", a common variation is extracting chunks between specific delimiter-like markers if they were strings.
    # However, since inputs are integers (indices), the most logical interpretation for "substrings ... that fall between" 
    # with multiple points implies: extract text found within each [start[i], end[i]] interval? Or the union of intervals?
    
    # Let's assume the request is to collect every substring whose *entirety* or specific parts lie between a defined global start and global end?
    # To make it "Pythonic" without ambiguous logic, I will interpret this as: 
    # Extract text segments that match a condition. Since no regex was asked for, but the prompt mentions "string slicing",
    # perhaps the intention is to find substrings between *any* start and end point provided in parallel lists?
    
    # Let's try a different angle often seen in coding tasks: 
    # Find all contiguous non-overlapping segments defined by matching (start_idx, end_idx) pairs.
    # But here we have two separate lists of points. 
    # Hypothesis 3 (Most robust for generic constraints): Extract text from the union of intervals [s_i, e_i].
    
    valid_indices = set()
    max_end_idx = max(end_points) if end_points else len(text) + 1
    
    # Collect all indices that are part of any defined range. 
    # We assume overlapping ranges just mean the text inside is kept? Or do we want substrings *strictly between* specific pairs provided as (start, end)?
    
    # Let's go with the interpretation: For each pair (s_i, e_i), extract the substring from s_i to e_i. 
    # If multiple pairs exist, return a list of these extracted strings? 
    # "Extract all substrings" suggests potentially overlapping or distinct ones.
    
    final_substrings = []
    for start_idx, end_idx in zip(start_points, end_points):
        if 0 <= start_idx < len(text) and start_idx + 1 <= min(end_idx, len(text)): 
            # Ensure we don't go out of bounds or negative length. 
            # Usually "between" implies exclusive? Or inclusive? Standard slice [start:end] is exclusive at end.
            substring = text[start_idx:end_idx+1 if end_idx < len(text) else None]  # Wait slicing handles bounds gracefully but let's be precise.
            
        # Correction: Python slices are robust, so we just need valid indices.

if __name__ == '__main__':
    pass
