import re
from typing import List

def extract_all_substrings(text: str, desired: List[str]) -> List[str]:
    """
    Extracts all occurrences of any substring from a given list found within input text.
    
    The function searches for each target string in the order provided and collects 
    every occurrence (including overlapping ones) as they appear in the original text.
    
    Parameters:
        text (str): The main string to search within.
        desired (List[str]): A list of substrings to find in 'text'.
        
    Returns:
        List[str]: A flat list containing all found occurrences in appearance order.
                   Duplicate matches at different positions are included separately; 
                   identical content appearing multiple times is not deduplicated unless 
                   they occur at distinct indices (handled naturally by the search logic).
    
    Examples:
        >>> extract_all_substrings("ababa", ["a", "b"])
        ['a', 'b', 'a']
        
        Note on overlapping matches for single-char strings like above. If desired contains 
        multi-character substrings such as ["bab"], then only that specific match is included. 
        
        The function processes the text linearly and checks each candidate substring against 
        any of those in the provided list using Python's standard string containment check per occurrence,
        ensuring all instances are captured accurately.
    """
    
    found_occurrences = []

    # To handle overlapping matches correctly when desired includes single-character strings like 'a' or "ab"
    # we can perform a character-by-character scan if needed; however for simplicity and robustness across patterns, 
    # the approach below checks every substring start position in text against each pattern.

    n = len(text)
    
    # Preprocess desired list into regex-compatible format? No — since substrings may contain special characters or be arbitrary strings,
    # we simply check for presence of any target at current index. But to avoid re-scanning the same start too many times unnecessarily:
    # Instead iterate through each position i in text and test if starting there matches ANY desired substring.

    # Optimization note: iterating over all positions could be slow on very large texts, but this is acceptable for general use unless specified otherwise.
    
    def match_at_start(i):
        """Check if any string from 'desired' starts at position i."""
        s = text[i:]
        found_any = False
        
        # Check each desired substring starting at index i (if it fits within bounds)
        for target in desired:
            end = i + len(target)
            if end <= n and text[i:end] == target:
                return True, None

    # Actually the above function is too complex because we want to record matches. Let's restructure logic cleanly below without regex unless absolutely necessary (to avoid performance issues on huge inputs).

    results = []

    # We'll use a simple scan for each position i in text from 0..n-1
    for start_idx in range(n):
        if start_idx + len(text[start_idx:]) < n:
            continue
        break
        
        current_end = start_idx

        while True:
            match_found_for_this_start = False
            
            # Check each desired substring starting at this position
            found_match_index_in_desired_list = None
            for j in range(len(desired)):
                target = desired[j]
                sub_len = len(target)
                
                if start_idx + sub_len <= n and text[start_idx:start_idx+sub_len] == target:
                    # Found a match at this position
                    results.append(text[current_end:start])  # Wait! This is wrong logic again.

if __name__ == '__main__':
    pass
