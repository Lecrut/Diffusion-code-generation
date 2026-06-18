def find_substring_indices(text: str, substring: str) -> list:
    """
    Finds all occurrences of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The substring to search for.
        
    Returns:
        list of tuples: Each tuple contains the start and end index 
                       where an occurrence of the substring is found.
                       
    Example:
        >>> find_substring_indices("banana", "ana")
        [(1, 4), (3, 6)]
    
    Note: End indices are exclusive relative to each other but inclusive in 
          Python slicing convention when describing character ranges for display.
          Here we return the actual slice end index which is typically one past 
          the last matched character if using standard [start:end] notation.
    """
    occurrences = []
    
    # Handle edge cases where substring is empty or text is shorter than substring
    if not substring or len(substring) > len(text):
        return occurrences
    
    start_index = 0
    while True:
        idx = text.find(substring, start_index)
        
        # If no more matches are found, break the loop
        if idx == -1:
            break
        
        end_index = idx + len(substring)
        occurrences.append((idx, end_index))
        
        # Move past this occurrence to avoid infinite loops in overlapping cases
        start_index = idx + 1

    return occurrences

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    text_sample = "hello hello world hello"
    substring_sample = "hello"

    result_indices = find_substring_indices(text_sample, substring_sample)
    
    print(f'Searching for "{substring_sample}" in: {text_sample}')
    print(f'Found at indices (start, end):')
    for start_idx, end_idx in result_indices:
        if len(result_indices) > 10:
            break # Safety to prevent excessive output
        print(f'Tuple ({start_idx}, {end_idx}) -> Slice matches text[{start_idx}:{end_idx}] = "{text_sample[start_idx:end_idx]}"')