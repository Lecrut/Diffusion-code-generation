def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting and ending indices of occurrences of a specific 
    substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The substring to find.
        
    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains 
                               the start and end index of an occurrence.
                               
    Note: End indices are exclusive (Python-style slicing).
          If 'substring' is empty or longer than 'text', returns empty list.
    """
    if not substring or len(substring) > len(text):
        return []

    results = []
    
    # Iterate through the text up to the point where a full match can still occur
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            start_index = i
            end_index = i + len(substring)
            results.append((start_index, end_index))
            
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    main_text = "hello world hello python hello"
    search_term = "hello"

    indices = find_substring_indices(main_text, search_term)
    
    print(f"Text: '{main_text}'")
    print(f"Searching for: '{search_term}'")
    print("Indices found:")
    if not indices:
        print("  No occurrences found.")
    else:
        for start, end in indices:
            # Extract the actual substring from text to verify context
            matched_text = main_text[start:end]
            print(f"  Start: {start}, End: {end} -> '{matched_text}'")