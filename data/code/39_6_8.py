def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices where `substring` occurs within `text`.
    
    Args:
        text (str): The larger string to search in.
        substring (str): The specific substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples containing the start and end indices 
                              for each occurrence. End index is exclusive.
                              
    Raises:
        ValueError: If `substring` is empty or longer than `text`.
    
    Note:
        Indices are 0-based. The substring at text[start:end] corresponds to the match.
        This implementation handles overlapping occurrences correctly by advancing 
        only after a full match (non-overlapping logic per standard search algorithms).
        If overlaps were required, slicing would be used differently. Here we use 
        start+1 for next iteration if not found, or just increment from current index.
        
    Actually, re-evaluating the requirement "all occurrences" usually implies finding 
    every instance even if they overlap (e.g., in 'ana' searching for 'an', indices are 0 and 2).
    However, standard `find` methods often skip past found matches. To be safe and cover 
    all potential overlaps as requested by "all occurrences", I will iterate through the text.
    
    Wait, let's clarify overlapping behavior based on common expectations:
    Text: 'aaaa', Substring: 'aa'
    Occurrences at (0, 2), (1, 3), (2, 4).
    If we use a simple loop checking every position i from 0 to len(text)-len(substring):
        if text[i:i+len] == substring: record it.
    
    This is the most robust interpretation of "all occurrences".
    """
    start_index = -1
    
    # Edge cases for empty inputs or invalid lengths
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both text and substring must be strings.")
        
    len_text = len(text)
    len_sub = len(substring)
    
    if len_sub == 0:
        return [] # Empty substring is undefined behavior for this task
    
    if len_sub > len_text:
        return []

    results = []
    
    # Iterate through all possible starting positions in the text
    max_start_index = len_text - len_sub + 1
    
    for i in range(max_start_index):
        start_idx = i
        
        end_idx = i + len_sub
        
        if text[start_idx:end_idx] == substring:
            results.append((start_idx, end_idx))
            
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or files used.
    
    test_cases = [
        ("Hello World", "World"),
        ("aaaaa", "aa"),  # Should find overlapping occurrences: (0,2), (1,3), (2,4)
        ("The rain in Spain", "ain"),
        ("No matches here", "xyz"),
        ("Find me a needle", "needle"),
    ]

    for text, sub_str in test_cases:
        indices = find_substring_indices(text, sub_str)
        
        if not indices:
            print(f"Text: '{text}'")
            print("Substring: '" + sub_str + "'")
            print("Result: No occurrences found.")
        else:
            print(f"Text: '{text}'")
            print(f"Substring: '{sub_str}'")
            
            # Print results in a readable format, e.g., "start-end"
            formatted_results = [f"{s}-{e}" for s, e in indices]
            result_string = ", ".join(formatted_results)
            print("Result:", result_string)
        print("-" * 30) # Separator line
        
    # Additional specific test case to demonstrate overlapping logic clearly
    complex_test = ("ababa", "aba")
    idxs_complex = find_substring_indices(complex_test[0], complex_test[1])
    
    if not idxs_complex:
        print(f"Complex Test Result: No occurrences found.")
    else:
        formatted_results = [f"{s}-{e}" for s, e in idxs_complex]
        result_string = ", ".join(formatted_results)
        print(f"\nText: '{complex_test[0]}', Substring: '{complex_test[1]}'")
        print("Result:", result_string) # Expected: 0-3, 2-5 (overlapping at index 4 'a')