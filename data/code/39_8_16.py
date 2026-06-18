import re

def find_substring_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns.
    
    For each pattern in the list, this function finds all non-overlapping 
    substrings within `text` that match the pattern (case-sensitive).
    
    Args:
        text: The input string to search for matches.
        patterns: A list of strings where each string is a regex pattern.
        
    Returns:
        A dictionary mapping each pattern (key) to a list of matched substrings (value).
        If no match is found, the value will be an empty list.
    """
    
    # Dictionary to store results for each pattern
    matches = {}
    
    for pattern in patterns:
        try:
            regex_obj = re.compile(pattern)
            
            all_matches = []
            current_match_index = 0
            
            while True:
                match = regex_obj.search(text, pos=current_match_index)
                
                if not match:
                    break
                
                matched_substring = match.group()
                # Check for overlap by setting the search position to 
                # one character after the end of this specific match.
                current_match_index = match.end()
                
                all_matches.append(matched_substring)
            
            matches[pattern] = all_matches
            
        except re.error as e:
            # In case a pattern is invalid, store None or handle appropriately based on needs.
            # Here we will just skip the error and return an empty list for that key to keep it robust.
            print(f"Warning: Invalid regex pattern '{pattern}'. Skipping.", file=__import__('sys').stderr)
            matches[pattern] = []

    return matches

if __name__ == '__main__':
    # Hard-coded sample values as per instructions
    
    input_text = "hello world hello python programming"
    
    search_patterns = [
        r'\\bhello\\b',      # Word boundary match for 'hello'
        r'h+l+d+',           # Matches strings containing h, l (non-greedy or specific counts) and d+? Let's simplify to just literal chars with regex logic. Actually let's use simple literals mixed with wildcards. 
                            # Pattern: Contains "l" followed by one or more digits if any exist in text, else nothing
        r'world',            # Literal match for 'world'
    ]

    results = find_substring_matches(input_text, search_patterns)
    
    print("Input Text:", input_text)
    print("\nPatterns and Matches:")
    for pattern, matches_list in results.items():
        if not isinstance(matches_list[0], str): # Handle None case from invalid regex logic above just in case
             matches_str = "Error processing pattern" 
        else:
            matches_str = ", ".join(repr(m) for m in matches_list if len(m)>0)