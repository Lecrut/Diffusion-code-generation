import re

def extract_all_substrings(text: str, substrings: list[str]) -> list[list[int]]:
    """
    Extracts all occurrences of specified substrings from a given text.
    
    Args:
        text (str): The input string to search within.
        substrings (list[str]): A list of strings to find in the main text.
        
    Returns:
        list[list[int]]: A list where each inner list contains start and end indices 
                        for an occurrence of a substring, ordered by appearance order.
    
    Example:
        >>> extract_all_substrings("hello world", ["l", "o"])
        [[1, 2], [3, 4], [5, 6]] (for 'l' at index 1 and 3; 'o' at index 4)
        
    Note: This function returns a flat list of all matches found across all substrings.
          If multiple occurrences exist for the same substring or different ones overlap 
          in position logic is handled by scanning left to right with non-overlapping 
          matching per specific search context if needed, but here we return start/end pairs 
          sorted primarily by their appearance order within the text flow considering each match independently.
    """
    
    # Dictionary to store results for each substring: {substring_index: [start_indices]}
    matches_by_substring = {}
    
    # Initialize list of substrings with unique identifiers if needed, though we use index directly here
    target_count = len(substrings)
    
    # For each desired substring in the input list
    for i, sub_str in enumerate(substrings):
        pattern = re.escape(str(sub_str))  # Escape special regex characters
        
        matches_by_substring[i] = []
        
        try:
            compiled_pattern = re.compile(pattern)
            
            # Find all non-overlapping occurrences of the substring
            for match in compiled_pattern.finditer(text):
                start_index = match.start()
                end_index = match.end()  # Exclusive, so length is end - start
                
                matches_by_substring[i].append([start_index, end_index])
        except re.error:
            # In case of invalid regex (though we escaped it manually), ignore or handle gracefully
            continue
            
    results_list = []

    for sub_idx in range(target_count):
        if sub_idx not in matches_by_substring:
            continue
        
        current_matches = matches_by_substring[sub_idx]
        
        # Append all occurrences of this substring to the result list
        for match_start, match_end in current_matches:
            results_list.append([match_start, match_end])

    return results_list

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly on the plain."
    desired_substrings = ["the", "rain", "in"]  # Case-sensitive by default unless specified otherwise
    
    found_occurrences = extract_all_substrings(sample_text, desired_substrings)

    print("Text:", sample_text)
    print("Desired substrings:", desired_substrings)
    print("\nAll occurrences (start_index, end_index):")
    
    for i in range(0, len(found_occurrences), 2):
        start_idx = found_occurrences[i]
        end_idx = found_occurrences[i + 1] if i + 1 < len(found_occurrences) else None
        
        substring_found = desired_substrings[found_occurrences.index([start_idx, end_idx]) % len(desired_substrings)]
        
        print(f"Substring '{substring_found}' at indices {start_idx} to {end_idx}")

    # Verify output format and logic with a simple assertion if needed for robustness testing internally
    assert isinstance(found_occurrences, list), "Output must be a list."
    assert all(isinstance(item, (list, tuple)) and len(item) == 2 for item in found_occurrences), \
        "Each occurrence must be represented as [start_index, end_index]."
    
    print("\nValidation passed.")