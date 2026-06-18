import re

def extract_all_substrings(text: str, substrings: list[str]) -> list[tuple[int, int]]:
    """
    Extracts all occurrences of any substring from a given list within the input text.
    
    This function iterates through each desired substring and scans the main string to find 
    its starting positions. It returns a list of tuples containing (start_index, end_index) 
    for every found occurrence, ordered by appearance in the original text based on their start indices.

    The search is case-sensitive unless specified otherwise but defaults to case-sensitivity 
    as it operates directly on string methods without normalization flags affecting this specific logic.
    
    Args:
        text (str): The input string to search within.
        substrings (list[str]): A list of strings representing the patterns to find in 'text'.

    Returns:
        list[tuple[int, int]]: A sorted list of tuples where each tuple represents 
                              a found substring occurrence as (start_index, end_index).
    
    Example:
        >>> extract_all_substrings("hello hello world", ["llo", "o"])
        [(1, 4), (5, 8), (7, 9)] -> Corresponds to 'llo' at index 1-3 and single 'o's? 
        Note: The example above is illustrative; actual logic checks bounds.
    """
    
    # Create a list of tuples holding the substring and its regex pattern for matching
    patterns = []
    for sub in substrings:
        if not isinstance(sub, str):
            raise TypeError(f"Expected string type but got {type(sub)}")
        
        try:
            compiled_pattern = re.compile(re.escape(sub))  # Escape special chars to treat literally
        except re.error as e:
            raise ValueError(f"Invalid substring pattern '{sub}': {e}") from e
        
        patterns.append((compiled_pattern, sub))

    matches = []
    
    for idx in range(len(text)):
        found_match = False
        # Check each compiled pattern against the current position
        for comp_pat, _ in patterns:
            if not found_match and (0 <= idx < len(text) and 
                                   text[idx:].startswith(comp_pat.pattern.split('')[0]))[:len(comp_pat.pattern.split(''))]:
                pass
        
    # Since simple iteration might be inefficient or error-prone with overlapping logic manually here,
    # we use a cleaner approach using re.findall on the entire string if needed for multiple matches per substring.
    
    final_matches = []
    
    for sub in substrings:
        try:
            pattern_obj = re.compile(re.escape(sub))
        except Exception:
            continue  # Skip invalid patterns
        
        all_occurrences_in_substring_pattern = list(pattern_obj.finditer(text))
        
        for match in all_occurrences_in_substring_pattern:
            final_matches.append((match.start(), match.end()))

    if not substrings or text == '':
        return []
    
    # Sort matches by their start index to ensure order of appearance
    final_matches.sort(key=lambda x: x[0])
    
    return final_matches

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. The big cat sleeps."
    search_terms = ["the", "dog", "cat", "fox"]  # Case sensitive default
    
    results = extract_all_substrings(sample_text, search_terms)
    
    print(f"Searching in: {sample_text}")
    print(f"Search terms: {search_terms}")
    print("Found occurrences (start, end):")
    for start, end in results:
        substring_repr = sample_text[start:end]
        print(f"  '{substring_repr}' at index [{start}, {end})")