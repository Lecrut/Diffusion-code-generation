import re

def find_pattern_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns.
    Returns a dictionary where keys are the pattern strings 
    and values are lists of all non-overlapping substrings in 'text' that match each pattern.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regular expression patterns as strings.

    Returns:
        dict[str, list[str]]: A dictionary mapping each pattern to a list of matching substrings.
                             If no matches are found for a pattern, the value is an empty list.
    """
    results = {}
    
    # Compile all regex patterns first for efficiency and error checking during compilation
    compiled_patterns = []
    valid_pattern_indices = []

    try:
        for idx, pattern_str in enumerate(patterns):
            compiled_regex = re.compile(pattern_str)
            compiled_patterns.append(compiled_regex)
            valid_pattern_indices.append(idx)
    except re.error as e:
        # If a pattern is invalid regex, we still include it but with an empty match list.
        # We'll map the original string index to handle this case gracefully if needed later, 
        # but for now just let's process only valid ones and skip errors or add them with empty lists?
        # The task implies patterns are given as strings; assuming they might be invalid regex too.
        results[pattern_str] = []

    # Process each text against all compiled (or skipped) patterns
    for idx, pattern in enumerate(patterns):
        if not re.compile(pattern).pattern:  # This check is redundant with try block above but safe
            continue
            
        matches_found = set()  # Use a set to avoid duplicate substrings due to overlapping captures
        
        current_regex = None
        valid_idx_in_list = -1

    # Re-do the loop correctly handling both invalid regex and collecting results
    
    for idx, pattern_str in enumerate(patterns):
        try:
            compiled_pattern = re.compile(pattern_str)
        except re.error:
            # Invalid regex is treated as having no matches.
            continue
            
        current_matches = []
        
        # Find all non-overlapping occurrences of the match object's group(0) in text
        for match in compiled_pattern.finditer(text):
            matched_substring = match.group(0)
            
            if not (matched_substring and len(matched_substring) > 0): 
                continue
                
            # Add to list. We use a set internally then convert back to ensure uniqueness per pattern?
            # The prompt says "list of all substrings". If multiple occurrences produce the same substring, should we include duplicates?
            # Usually in such tasks, if 'a' appears twice matching pattern X, you might want ['a', 'a']. 
            # But often unique is preferred. Let's stick to collecting every occurrence found by finditer().
            
            current_matches.append(matched_substring)

        results[pattern_str] = current_matches
        
    return results

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly in the plain."
    
    # Sample list of patterns (some valid, one invalid to test robustness if desired, but let's keep them all valid for clarity)
    sample_patterns = [
        r"ain",           # Matches 'rain', 'Spain', 'plain' etc.
        r"\b\w+in\b",     # Words ending in 'in': rain, Spain, plain (if treated as word boundary logic works differently with regex) 
                        # Actually \b matches non-word chars or start/end of string. 'ain' is inside words mostly unless at end/start?
                        # Let's use simpler patterns for clarity:
        r"\d+",           # Digits (none expected in text, will return empty list)
        r"e",             # Single letter e
    ]

    output = find_pattern_matches(sample_text, sample_patterns)

    print("Pattern Matches:")
    for pattern, matches in output.items():
        if not isinstance(matches, list): 
            continue
            
        print(f"\nPattern: {pattern}")
        print(f"Matches ({len(matches)} found):")
        
        # Ensure we don't duplicate identical substrings unless they are distinct occurrences? 
        # The finditer returns all non-overlapping matches. If pattern is 'e', it finds every e in text as a separate match object.
        # We want the substring itself repeated if multiple times occur? Or just unique values?
        # Re-reading: "list of all substrings". Usually implies list of found strings, possibly with duplicates based on position.
        
        print(matches)

    # Demonstrate output structure explicitly for verification logic clarity in main block
    assert isinstance(output, dict), "Output must be a dictionary"
    for pattern_key in sample_patterns:
        if pattern_key not in output: 
            continue
            
        matches_list = output[pattern_key]
        type_check_passed = isinstance(matches_list, list) and all(isinstance(s, str) for s in matches_list)
        
        assert type_check_passed, f"Pattern {pattern_key} should return a list of strings."

    print("\nAll assertions passed.")