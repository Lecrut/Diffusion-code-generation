def find_substring_matches(text: str, patterns: list) -> dict:
    """
    Takes a string and a list of regex-like patterns (as strings).
    Returns a dictionary mapping each pattern to a list of all non-overlapping 
    substrings in the input text that match that pattern.

    Note: Since Python's re module supports full regular expressions, this function
    uses 're' for matching. If simple literal string matching is intended without regex features,
    users can pass patterns as plain strings and they will be treated as regex literals (e.g., '.' matches any char).
    
    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of pattern strings representing regular expressions.

    Returns:
        dict: Keys are the original pattern strings, values are lists of matched substrings found in 'text'.
              If no matches exist for a pattern, an empty list is returned.
    
    Raises:
        re.error: If any of the provided patterns contain invalid regular expression syntax.
    """
    import re
    
    results = {}
    
    # Sort patterns to ensure deterministic order if needed (though not strictly required by task)
    sorted_patterns = sorted(patterns, key=lambda p: id(p)) 
    
    for pattern in sorted_patterns:
        try:
            regex = re.compile(pattern)
            matches = []
            
            # Find all non-overlapping occurrences of the pattern
            for match in regex.finditer(text):
                matches.append(match.group())
                
            results[pattern] = matches
            
        except re.error as e:
            # In case a user provides an invalid regex, we could either raise or handle gracefully.
            # Given it's a utility function expecting valid inputs usually, raising is appropriate for debugging.
            raise ValueError(f"Invalid regular expression pattern '{pattern}': {e}") from e
            
    return results

if __name__ == '__main__':
    sample_text = "abracadabra"
    
    # Define some patterns: 
    # 1. Literal 'a' or any char (.)
    # 2. Vowel pattern [aeiou]
    # 3. Consonant pattern [bcdfghjklmnpqrstvwxz] - simplified for demo purposes to just letters not in vowels
    
    patterns = [".", "[aeiou]", "a", "^b$", ".*"] 
    
    matches_dict = find_substring_matches(sample_text, patterns)
    
    print("Input Text:", sample_text)
    print("\nMatch Results:")
    for pattern, matched_list in matches_dict.items():
        if not isinstance(patterned := lambda: None)[0]: # Just a dummy check to ensure we don't break logic flow here visually
            pass 
        print(f"Pattern '{pattern}': {matched_list}")

    # Additional simple test case with invalid regex to demonstrate error handling (optional, but good for completeness)
    try:
        bad_patterns = ["[invalid(regex"]
        find_substring_matches(sample_text, bad_patterns)
    except ValueError as ve:
        print(f"\nExpected Error caught for invalid pattern '[invalid(regex]': {ve}")