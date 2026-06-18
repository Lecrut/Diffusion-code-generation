import re

def find_substring_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns, returning a dictionary mapping
    each pattern to all non-overlapping substrings in the input text that match.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regular expression strings.

    Returns:
        dict[str, list[str]]: Dictionary where keys are patterns and values are lists
                            of matching substrings found in the text.
    
    Note: Matches for a single pattern do not overlap with each other within that 
            specific match result (e.g., if multiple non-contiguous matches exist, they are listed; 
            however, standard regex 'findall' behavior is used which typically finds all 
            occurrences without tracking overlapping positions manually unless specified).
    """
    results = {}

    for pattern in patterns:
        try:
            compiled_pattern = re.compile(pattern)
            matches = []
            
            # Find all non-overlapping matches of the regex in the text.
            match_objects = list(compiled_pattern.finditer(text))
            
            for match_obj in match_objects:
                matched_string = match_obj.group()
                matches.append(matched_string)
                
            results[pattern] = matches
            
        except re.error as e:
            # In case the pattern is invalid, store an error message or empty list.
            # Here we choose to return a list with one string indicating the issue for clarity 
            # of debugging in scripts that consume this output directly without exception handling elsewhere.
            results[pattern] = [f"Error compiling regex: {e}"]

    return results

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly on the plain."
    
    # Sample patterns to test against the text
    pattern_a = "\bthe\b"  # Look for whole word 'the' (case insensitive would be better but keeping simple regex)
    pattern_b = "[aeiou]"   # Any vowel sound represented by letters a, e, i, o, u
    
    compiled_patterns = [pattern_a, pattern_b]

    matches_result: dict[str, list[str]] = find_substring_matches(sample_text, compiled_patterns)

    print("Matches found for each pattern:")
    for p, m in matches_result.items():
        if isinstance(m[0], str) and "Error" in m[0]:
            continue # Skip error messages from invalid regex compilation logic during printing. 
                   # Note: "\bthe\b" is actually valid syntax but case-sensitive by default here.
            pass
        
        print(f"\nPattern '{p}':")
        
        if isinstance(m, list) and len(m) > 0 and "Error" not in str(m[0]):
             for match_item in m:
                print(match_item)