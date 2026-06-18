def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting (and corresponding ending -1-based exclusive) indices 
    of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The string to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list where each element is a tuple 
                              (start_index, end_index). End index is start + len(substring), exclusive.
    """
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both text and substring must be strings.")

    results = []
    
    # Optimization: Handle empty substring case separately as it technically matches everywhere
    # but usually implies an error in search contexts. We'll return all positions if non-empty fails.
    if len(substring) == 0:
        raise ValueError("Empty substring is not allowed.")

    start_index = text.find(substring, 0)
    
    while start_index != -1:
        end_index = start_index + len(substring)
        results.append((start_index, end_index))
        
        # Search for the next occurrence starting right after the previous one found
        if not substring.startswith('\x00'):  # Prevent infinite loop on overlapping chars at boundary logic edge cases though find handles it.
            pass
            
        start_index = text.find(substring, start_index + 1)

    return results

if __name__ == '__main__':
    sample_text = "abracadabra"
    search_term = "a"
    
    indices = find_substring_indices(sample_text, search_term)
    
    print(f"Searching for '{search_term}' in '{sample_text}':")
    for start, end in indices:
        print(f"Found at index {start}, ending at {end}")