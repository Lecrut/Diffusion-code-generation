import re

def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting and ending indices of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains the 
                               start and end index of an occurrence of the substring.
    
    Note: End indices are exclusive if using Python's standard slicing convention (i.e., [start:end]).
          If you want inclusive ending indices, add 1 to the second element in the returned tuple.
    """
    if not text or len(text) == 0 and substring != "":
        return []

    results = []
    
    # Handle empty substring case - technically matches everywhere but usually undefined behavior.
    # Assuming non-empty substring for practical utility, returning empty list for empty input.
    if not substring:
        # If an empty string is provided as search term, we could argue it exists at every position,
        # but typically this function is used to find meaningful patterns. 
        # We will treat a 0-length substring differently based on common expectations (usually none or specific convention).
        # For robustness: if substring length is 0, return indices of empty matches? 
        # Let's assume standard behavior: only search for non-empty strings unless specified otherwise.
        pass

    i = 0
    while True:
        idx = text.find(substring, i)
        
        # If find returns -1 (not found), exit the loop
        if idx == -1:
            break
        
        # Calculate start and end indices inclusive or exclusive based on convention.
        # Standard Python list slicing [start:end] excludes 'end'. 
        # The task asks for "ending index", which in mathematics often means inclusive.
        # However, to match standard programming conventions unless specified otherwise, we'll provide 
        # the start and (start + length). If you want inclusive end, add 1 here.
        
        length = len(substring)
        start_index = idx
        end_index_inclusive = start_index + length
        
        results.append((start_index, end_index_inclusive))
        
        i = idx + 1 # Move index forward to find overlapping occurrences (e.g., "ana" in "banana")

    return results

if __name__ == '__main__':
    sample_text = "abcdeabcdefabcedcba"
    search_term = "abcd"
    
    indices = find_substring_indices(sample_text, search_term)
    
    print(f"Text: {sample_text}")