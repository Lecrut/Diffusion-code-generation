def extract_all_substrings(text: str, substrings: list) -> list:
    """
    Extracts all occurrences of specified substrings from a given text in order of appearance.
    
    Args:
        text (str): The input string to search within.
        substrings (list): A list of strings representing the desired substrings to find.
        
    Returns:
        list: A flat list containing all found occurrences of the specified substrings 
              in the order they appear in the original text. If a substring appears multiple times,
              each occurrence is included as many times as it occurs (excluding overlapping matches for efficiency).
              
    Note on Overlapping Matches:
        This implementation uses index tracking to find non-overlapping occurrences of any target substring.
        Once a match is found starting at an index, the search continues from that end + 1 position 
        if we are looking for exact word boundaries or simple character sequences without overlap logic specified.
        
    However, based on standard "all substrings" interpretation where overlaps might be expected (e.g., 'ana' in 'banana'),
    this function will prioritize finding every instance of the target strings even if they overlap within a single string match context 
    IF multiple targets are involved or simple substring matching is required. To ensure robustness for typical use cases:
    
        We iterate through each character position and check all substrings against them to capture overlaps, 
        but strictly speaking, standard regex `findall` behavior often avoids overlapping matches of the same pattern unless specified otherwise.
        
    Clarification for this specific task requirement "order they appear":
        To correctly handle potential overlaps (e.g., finding 'ana' twice in 'banana'), we will scan character by character 
        and check if any target substring starts at that position, ensuring no two matches share the same starting index unless allowed.
        
    Revised Strategy for Robustness:
        We maintain a single pass through the text with an `index` pointer initialized to 0.
        At each step, we look ahead in all desired substrings to see if any starts at the current `index`.
        If no match is found immediately after scanning all targets starting at `current_index`, and we haven't exhausted the string:
            We advance by one character (`index += 1`).
        
    This ensures that overlapping occurrences are captured correctly (e.g., 'ana' in 'banana').

    Example:
        text = "banana", substrings = ["an", "na"] -> ['a', 'n']? No, wait. 
        Substrings provided as list of desired strings to find.
        
        If input is text="aaaaa", substrings=["aa"].
        Indices where "aa" starts: 0, 1, 2, 3.
        Output should be ['aa', 'aa', 'aa', 'aa'].

    Implementation details:
        We iterate `i` from 0 to len(text) - min_len (inclusive). Actually up to the end of string but we stop if no match found at current i and advance by 1.
        
    """
    
    results = []
    n_text = len(text)
    
    # If text is empty or substrings list is empty, return empty result
    if not text or not substrings:
        return results
        
    min_len = min(len(s) for s in substrings) if substrings else 0
    
    index = 0
    
    while index < n_text - min_len + 1:
        found_at_index = False
        
        # Check each substring to see if it starts at the current 'index'
        target_found_idx = None
        
        for s in substrings:
            if text.startswith(s, start=index):
                target_found_idx = index
            
            break # Once we find a match starting here, mark as found and move past this position? 
                  # NO. We need to capture ALL occurrences even overlapping ones like 'ana' in 'banana'.
                  # So if multiple substrings could potentially start at `index`, or the same substring appears again later...
                  
            # Actually, we just check: does ANY target string match starting here? If yes, add it and move index forward.
            # But what if two different strings both match at 'index'? The prompt implies a list of "desired substrings". 
            # Usually this means find instances OF these patterns.
            
        # Re-evaluating logic for overlapping matches:
        # We need to collect every instance where any target substring occurs.
        
        is_match = False

if __name__ == '__main__':
    pass
