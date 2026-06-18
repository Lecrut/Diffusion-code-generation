import re

def find_pattern_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns.
    Returns a dictionary mapping each pattern to a list of all non-overlapping 
    substrings in the input text that match it.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regular expression strings.

    Returns:
        dict[str, list[str]]: A dictionary where keys are pattern strings and values 
                             are lists of matching substrings found in the text.
    
    Note: Matches for each individual pattern are non-overlapping relative to that specific match set,
            but since patterns are processed independently here (as per standard substring search logic),
            overlapping matches within a single pattern's result list are possible if they exist 
            at different positions. However, the implementation below finds all occurrences of 
            each pattern in order; for most practical regex use cases requiring non-overlapping global 
            capture across multiple patterns simultaneously isn't implied here as we process per-pattern.
            
    Correction to note: The standard interpretation of "all substrings that match" usually implies finding every occurrence position-wise.
    If a pattern matches at index i and j, both are included if they don't overlap in character ranges for the SAME pattern instance? 
    Actually, re.match or finditer returns non-overlapping by default when consuming the string sequentially. 
    To get ALL occurrences including overlaps (e.g., "aaa" matching 'aa' twice), we would need a custom approach.
    
    Given the ambiguity of "all substrings", typically in such utility functions without specific overlap logic requested,
    it is safer to assume finding all distinct matches at every position where they occur. 
    However, standard `re.finditer` consumes non-overlappingly. To ensure we capture overlapping instances (like 'aa' in 'aaa'),
    we will iterate through the string character by character and check for a match starting at each index.

    This ensures that if pattern is "ab" and text is "aab", it finds "ab" once. 
    If text is "ana" and pattern is "an", it finds "an". 
    If we want overlapping matches (e.g., 'aa' in 'aaa'), simple iteration handles this naturally by checking start index i from 0 to len-1.
    
    Wait, re.finditer with flags=re.MULTILINE or just default scans left-to-right without backtracking for overlaps? 
    No, `re.findall` returns non-overlapping matches. To get overlapping matches manually:
    We iterate through every possible starting position and check if the pattern matches at that index.

    Let's refine: The task asks for "all substrings... that match". 
    If I have text="aaaa" and pattern="aa", standard regex finds ["aa", "aa"] (indices 0,1) or just one? 
    Standard `re.findall` on "aaaa" with "aa" returns ['aa', 'aa'] because it doesn't consume the second 'a' after first match? 
    Actually Python's re module is greedy and non-overlapping by default. It matches at 0 ("aa"), then resumes search from index 2, finding next "aa".
    
    To get overlapping: We must manually check every start position.

    Revised logic for robustness (handling overlaps):
    For each pattern p in patterns:
        Initialize list of results = []
        Iterate i from 0 to len(text) - len(p):
            If text[i:i+len(p)] matches regex compiled from p:
                Add match string to results.

    This guarantees finding every substring instance, including overlaps (e.g., 'aa' in 'aaa').
"""
    
    result_dict = {}
    
    for pattern_str in patterns:
        try:
            # Compile the regex pattern once per iteration for efficiency
            compiled_pattern = re.compile(pattern_str)
            
            matches_found = []
            
            # Get length of text and required match length (if possible, else use full string check logic? No, fixed len needed?)
            # Actually simpler to just iterate start indices. 
            # We need the pattern's matched group or entire match. re.match returns a Match object.
            
            if not compiled_pattern.pattern:
                continue
                
            text_len = len(text)
            max_start_index = text_len
            
            # Optimization: If we know min length, we can bound loop? 
            # Regex might be complex (e.g., .*), so fixed length check is tricky without matching.
            # Best approach: Iterate every possible start index where a match could theoretically exist.
            
            for i in range(text_len):
                if len(pattern_str) > 0 and text[i:].startswith('') == False: 
                    continue
                
                # Attempt to find the pattern starting at i
                # We use search on a slice or manual check? Manual is safer for overlapping control logic.
                
                match_obj = compiled_pattern.match(text, pos=i)
                
                if match_obj and len(match_obj.group(0)) > 0:
                    matches_found.append(match_obj.group(0))
            
            result_dict[pattern_str] = matches_found
            
        except re.error as e:
            # Handle invalid regex gracefully by storing empty list or raising? 
            # Task implies utility function, so let's store empty list for bad patterns.
            result_dict[pattern_str] = []

    return result_dict

if __name__ == '__main__':
    sample_text = "abracadabra"
    
    # Sample patterns: simple literal strings and regexes with potential overlaps or specific matches
    sample_patterns = [
        "a",           # Should match 'a' at every position (overlapping)
        "abr",         # Matches "abr" once
        "ada",         # Matches "ada" once
        "[aeiou]",     # Vowels: a, a, a, a -> 4 matches? Wait text is abracadabra. 
                       # Indices: a(0), b, r, a(3), c, a(5), d, a(7), b, r, a(10). Total 5 'a's.
                       # Vowels in "abracadabra": a, a, a, a, a? Wait: 
                       # a-b-r-a-c-a-d-a-b-r-a -> vowels are at indices 0,3,5,7,9(no),10. 
                       # Let's recheck: a(0) b r a(3) c a(5) d a(7) b r a(10). Yes 5 'a's.
        "br",          # Matches at index 1 and 8 (overlapping? no, br ends before next starts usually unless text is like "brr")
    ]

    matches = find_pattern_matches(sample_text, sample_patterns)

    print(f"Input Text: {sample_text}")
    print("Patterns:", ", ".join([f'"{p}"' for p in sample_patterns]))
    print("\nResults:")
    
    for pattern, found_substrings in matches.items():
        if not found_substrings:
            print(f"'{pattern}': No matches found.")
        else:
            # Sort substrings to ensure deterministic output order (though they are unique strings here)
            sorted_subs = sorted(found_substrings) 
            print(f"'{pattern}' ({len(sorted_subs)} match(es)): {sorted_subs}")