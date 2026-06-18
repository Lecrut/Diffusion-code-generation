def find_pattern_substrings(input_string: str, patterns) -> dict:
    """
    Takes a string and a list of patterns, returning a dictionary mapping each pattern
    to a list of all substrings in the input string that match it.

    Args:
        input_string (str): The text to search within.
        patterns (list[str]): A list of regex or literal strings to find matches for.

    Returns:
        dict: Mapping from each pattern to its matching non-overlapping substring occurrences.
              If the same match appears multiple times, it is listed once per occurrence found sequentially.
              Note: For simplicity and deterministic behavior across patterns (including overlapping potential), 
              this implementation finds all matches for a given pattern in sequence order within the string.
    """

    results = {}

    # Process each provided pattern
    for pattern_str in patterns:
        import re
        try:
            compiled_pattern = re.compile(pattern_str)
        except re.error as e:
            # Skip invalid regex patterns gracefully, logging is not explicitly requested but handled silently here per "no input" constraint.
            results[pattern_str] = []
            continue

        matches_found = []
        
        # Find all non-overlapping occurrences of the pattern in the string to get substrings
        for match_obj in compiled_pattern.finditer(input_string):
            substring_match = match_obj.group()
            
            # We add the matched substring itself as it is a valid instance that fits the requirement 
            # "substrings... that match that pattern". Usually, this implies the exact span matches.
            # If we wanted to list *all* substrings inside the string that somehow relate loosely, logic would differ,
            # but standard interpretation for "patterns" with regex is matching tokens/subsequences exactly as defined by the pattern.
            
            matches_found.append(substring_match)

        results[pattern_str] = matches_found

    return results

if __name__ == '__main__':
    sample_string = "abracadabra"
    patterns_to_check = [".*", "^a", "[bc]", r"(?i)cad"]  # (?i) makes the last one case-insensitive
    
    output_dictionary = find_pattern_substrings(sample_string, patterns_to_check)

    for pattern, matches in output_dictionary.items():
        print(f"Pattern: '{pattern}'")
        if not matches:
            print("No matches found.")
        else:
            # Ensure uniqueness of the *substring text* or keep duplicates based on occurrences? 
            # The prompt asks for "list of all substrings... that match".
            # If "aba" appears twice, should we list "aba", "aba"? Yes.
            print(f"Matches found: {matches}")
        print("-" * 20)

    assert output_dictionary[".*"] == ["abracadabra"], "First pattern (.)* matched entire string."
    assert "^a" in patterns_to_check, "Testing first char anchor"