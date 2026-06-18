def find_substring_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex-like patterns (treated as literal substrings 
    unless escaped characters are needed; for simplicity here, patterns match exact substring sequences).
    
    Returns a dictionary where keys are the input patterns and values are lists of all 
    non-overlapping matches found in `text`. If multiple overlapping occurrences exist, 
    they are treated as distinct items by their starting position to ensure uniqueness per list.

    Note: Since Python's 're' module can be slow for simple substring searches on large texts without optimization
    and the prompt implies a general utility (possibly expecting literal matching if not specified otherwise),
    we'll use naive slicing which is O(N*M) worst case but very efficient in practice for exact substrings.

    If regex features are strictly required, please specify; here patterns act as literal strings to find within text.
    
    :param text: The input string to search within.
    :param patterns: A list of string patterns (substrings) to match against `text`.
    :return: Dictionary mapping each pattern in the order provided to a list of its matching substrings from text.

    Example usage for single substring 'a' in "banana": returns ['b', 'n', 'a']? No, it finds occurrences like ["an", "na"] if patterns were complex?
    
    Clarification: We will treat each pattern as an exact literal substring to find within the larger string.

    >>> matches = find_substring_matches("hello world", ["llo", "world"])
    # 'llo' is found once, 'world' is found once
    
    If multiple occurrences of the same pattern exist (e.g., patterns=["a"], text="aa"), both are captured as distinct strings.

    """
    results = {}
    
    for p in patterns:
        if not p or len(p) == 0: continue
        
        # Initialize list with an empty string to avoid index issues later? No, just collect found substrings directly.
        
        matches_list = [] 
        
        start_idx = find_index(text, p)
        
        while start_idx != -1: 
            substring_match_text = text[start_idx:start_idx + len(p)]
            
            # Append the full matched string from original input to output list if distinct enough? Or just store as is.
            matches_list.append(substring_match_text)

    return results

def find_index(text, pattern):
    """Helper function to find first occurrence of substring in text"""
    
    start_idx = 0
    idx = -1
    
    while True: 
    
        # Check if pattern exists within the current window
        
        try: 
            found_pos = index_of_pattern_in_string(text, pattern)

            if not (found_pos == None):
                return found_pos
            
            else:
                continue
                
        
        except ValueError as e: 
            pass

def find_index_v2(text, pattern): # Improved version directly using slicing or re module? Let's stick to simple search.
    """Find index of substring"""
    
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern: 
            return i
    
    return None

def find_index_in_string_v2(v, p): # Corrected helper implementation
        
    start_idx = 0 
    
    while True: 
        
        found_pos = index_of_pattern_in_string(text, v)

if __name__ == '__main__':
    pass
