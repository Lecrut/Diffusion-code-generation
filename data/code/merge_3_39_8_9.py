import re

def find_substrings_by_pattern(text: str, patterns: list) -> dict:
    """
    Takes a string `text` and a list of regex-like strings (`patterns`).
    Returns a dictionary where keys are the pattern strings and values 
    are lists of all non-overlapping substrings in `text` that match each respective pattern.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regex pattern strings to use for matching.

    Returns:
        dict[str, list]: Mapping from each pattern to its list of matched substrings.
    
    Note:
        Matching is performed using regular expressions. Overlapping matches 
        are not counted as separate entries; once a match begins at an index, 
        subsequent characters in that sequence are skipped for the same pattern instance.
        
        If no substring matches a pattern, its entry will be an empty list.
    """

    results = {pattern: [] for pattern in patterns}
    
    for idx, pattern_str in enumerate(patterns):
        try:
            compiled_pattern = re.compile(pattern_str)
        except re.error as e:
            # Handle invalid regex gracefully by returning empty list for this pattern
            continue
            
        current_idx = 0
        matches_found_for_this_run = []

        while True:
            match_obj = compiled_pattern.search(text, start=current_idx)
            
            if not match_obj:
                break
                
            matched_substring = match_obj.group()
            results[pattern_str].append(matched_substring)
            
            # Move the index past this specific match to prevent overlapping 
            # matches for the same pattern instance (standard non-overlapping behavior).
            current_idx = match_obj.end()

    return results

if __name__ == '__main__':
    input_string = "abracadabra"
    patterns_list = [r"a", r"c.*d", r"[aeiou]+"]

    output_map = find_substrings_by_pattern(input_string, patterns_list)

    print("Patterns:", patterns_list)
    for pattern in patterns_list:
        matches = output_map[pattern]
        if not isinstance(matches, list):
            continue  # Skip invalid cases (shouldn't happen with current logic)
        
        is_empty = len(matches) == 0
        
        if is_empty:
            print(f"\nPattern '{pattern}' matched nothing.")
        else:
            for match in matches:
                print(f"Found substring matching pattern '{pattern}': {match}")

    # Additional verification block to ensure the module runs correctly without external input
    assert isinstance(output_map, dict), "Result must be a dictionary."
    
    assert patterns_list[0] in output_map, f"Pattern '{patterns_list[0]}' missing from result."