def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The string to find occurrences of.
        
    Returns:
        A list of tuples where each tuple contains the start and end index 
        (inclusive) for an occurrence of the substring. If not found, returns empty list.
    
    Note on indices: Python strings are 0-indexed. For a match at text[start:start+len(substring)],
    this function returns (start, start + len(substring)).
    """
    if not substring or not isinstance(text, str) or not isinstance(substring, str):
        return []

    results = []
    
    # Handle edge case where substring is empty string per standard convention 
    # (usually implies infinite matches at every position), but we'll treat it as no match
    # to avoid ambiguity unless specified otherwise. If strict behavior for empty string needed:
    if len(substring) == 0:
        return []

    start_index = 0
    text_length = len(text)
    substring_length = len(substring)

    while True:
        index = text.find(substring, start_index)
        
        # If no more occurrences are found (find returns -1), break loop.
        if index == -1:
            break
        
        end_index = index + substring_length
        results.append((index, end_index))
        start_index = index + 1

    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    main_text = "hello world hello python hello"
    search_term = "hello"

    indices = find_substring_indices(main_text, search_term)

    print(f"Text: '{main_text}'")
    print(f"Searching for: '{search_term}'")
    print("Occurrences (start_index, end_index):")
    
    if not isinstance(indices, list):
        print("Error: Function returned unexpected type.")
    else:
        # Iterate and display results. If no matches found, this block prints nothing after the header.
        for start, end in indices:
            print(f"  Start index: {start}, End index: {end}")
            
            # Optional verification output (commented out to keep it clean)
            # assert main_text[start:end] == search_term
            
    if not indices and len(main_text) > 0:
        print("No occurrences found.")