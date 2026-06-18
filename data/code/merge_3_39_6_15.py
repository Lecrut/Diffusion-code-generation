def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting and ending indices of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains 
                               the start and end indices of an occurrence.
    
    Raises:
        ValueError: If both text and substring are empty strings.
    """
    if not text or not substring:
        raise ValueError("Both 'text' and 'substring' must be non-empty strings.")

    results = []
    index = 0
    
    while True:
        start_index = text.find(substring, index)
        
        # If no more occurrences are found, break the loop
        if start_index == -1:
            break
        
        end_index = start_index + len(substring)
        results.append((start_index, end_index))
        
        # Move to the next position after this occurrence to find overlapping matches
        index = start_index + 1

    return results

if __name__ == '__main__':
    sample_text = "ababcabd"
    sample_substring = "aba"
    
    indices = find_substring_indices(sample_text, sample_substring)
    
    print(f"Text: '{sample_text}'")
    print(f"Substring: '{sample_substring}'")
    print("Occurrences (start, end):", indices)