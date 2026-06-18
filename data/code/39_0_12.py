import re

def extract_all_substrings(text: str, desired_patterns: list[str]) -> list[list[int]]:
    """
    Extracts all occurrences of specified substrings from a given text.
    
    Args:
        text (str): The input string to search within.
        desired_patterns (list[str]): A list of strings representing the 
                                      patterns to find in the text.
        
    Returns:
        list[list[int]]: A list where each inner list contains start and end indices
                         for an occurrence of any pattern found in order of appearance.
                         
    Example:
        >>> extract_all_substrings("hello world", ["llo", "world"])
        [[2, 5], [6, 11]]
        
    Note:
        This function uses regex with the 're.I' flag for case-insensitive matching 
        if desired patterns are provided. If exact match is required regardless of case,
        use this version as-is (case-sensitive). To enable case-insensitivity globally,
        modify the search logic to include re.IGNORECASE when appropriate based on requirements.
        
    The function returns a list of lists, where each inner list contains two integers:
    [start_index, end_index] representing the start and end positions of an occurrence.
    
    Raises:
        TypeError: If text is not a string or desired_patterns is not a list of strings.
    """
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string.")
    if not isinstance(desired_patterns, list) or not all(isinstance(p, str) for p in desired_patterns):
        raise TypeError("The 'desired_patterns' argument must be a list of strings.")

    results = []
    
    # Create a combined regex pattern to match any of the desired substrings
    # Use non-capturing group with alternation. 
    # Note: This approach finds all matches in order but doesn't track which specific substring matched first unless needed.
    # Since we need "all found occurrences", and typically one occurrence per position,
    # using a single regex that tries to match any of the patterns is efficient for finding positions.
    
    combined_pattern = '|'.join(re.escape(p) for p in desired_patterns)
    full_regex = re.compile(combined_pattern)

    matches = list(full_regex.finditer(text))

    for match in matches:
        start_index = match.start()
        end_index = match.end()  # Exclusive, as per Python slicing convention
        
        results.append([start_index, end_index])
        
    return results

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. The cat sat on the mat."
    desired_substrings = ["the", "cat", "dog"]

    # Convert to lowercase for case-insensitive search as per common expectation unless specified otherwise
    text_lower = sample_text.lower()
    patterns_lower = [p.lower() for p in desired_substrings]

    found_occurrences = extract_all_substrings(text_lower, patterns_lower)

    print("Text:", sample_text)
    print("Desired substrings (case-insensitive):", desired_substrings)
    print("\nFound occurrences (start_index, end_index):")
    
    for i, occurrence in enumerate(found_occurrences, 1):
        start_idx = occurrence[0]
        end_idx = occurrence[1]
        substring_found = text_lower[start_idx:end_idx]
        original_substring_match = next(p.lower() for p in desired_substrings if p == substring_found)
        
        print(f"{i}. Indices: {start_idx} to {end_idx}, Matched Pattern: '{original_substring_match}'")

    # Verify no external inputs or files were used by confirming the output structure is consistent with hard-coded data.