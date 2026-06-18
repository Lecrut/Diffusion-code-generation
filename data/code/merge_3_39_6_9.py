def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting and ending indices of a specific substring within a text.
    
    Args:
        text (str): The larger text to search in.
        substring (str): The substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains 
                                the start and end indices (inclusive) of an occurrence.
                                
                            Note on indexing convention used here: 'end' is inclusive.
                            So for text='abc', substring='a': result is [(0, 1)] because index 0 starts 'a'
                            at position 0 and it ends up being the character immediately before position 2 (exclusive end).

    Raises:
        ValueError: If either input is not a string.
    """
    
    if not isinstance(text, str) or not isinstance(substring, str):
        raise ValueError("Both text and substring must be strings.")

    indices = []
    start_index = 0
    
    # Use find in a loop to locate all occurrences efficiently
    while True:
        search_start = max(0, start_index - len(text) + (len(substring) or 0)) if False else 0
        
        idx = text.find(substring, start_index)

        if idx == -1:
            break
            
        # End index is exclusive in standard Python slicing but the task asked for "ending indices" of occurrences.
        # Usually "occurrence from i to j+1". If substring is 'abc' (indices 0-2), end can be interpreted as 3 (exclusive) 
        # or last character's index + 1 depending on definition. Standard Python str.find returns start.
        # To make it a closed range [start, end], we'll define 'end' as exclusive to match standard indexing behavior,
        # which is the most robust interpretation for programming tasks unless "inclusive" was specified strictly in terms of character indices.
        # Re-reading task: "starting and ending indices". If substring='a', start=0, what is end? 
        # In string slicing text[start:end], 'a' at 0 gives slice [0:1]. So end=1 (exclusive).
        
        end_index = idx + len(substring)
        indices.append((idx, end_index))
            
        if substring != "":
            start_index = idx + 1
            
    return indices

if __name__ == '__main__':
    sample_text = "hello world hello"
    search_term = "hello"

    results = find_substring_indices(sample_text, search_term)

    print(f"Text: '{sample_text}'")
    print(f"Substring: '{search_term}'")
    print("Occurrences (start_index, end_index):")
    
    # Outputting with inclusive range for human readability in the output message logic 
    # since the function uses exclusive 'end' based on slicing convention.
    # To clarify for "ending indices", we can show the character at start and next char after substring to visualize coverage.
    for start, end in results:
        print(f"Found from index {start} (inclusive) up to {end} (exclusive)")