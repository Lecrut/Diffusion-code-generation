def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices where `substring` occurs in `text`.
    
    Args:
        text (str): The larger text to search within.
        substring (str): The specific substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples containing the start and end indices 
                              for each occurrence. End index is exclusive.
    """
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both text and substring must be strings.")

    results = []
    
    # Handle edge case where substring is empty string
    # Convention: an empty substring matches at every position up to len(text)
    if len(substring) == 0:
        for i in range(len(text) + 1):
            results.append((i, i))
        return results

    start = 0
    while True:
        # Find the next occurrence of substring starting at or after current position
        idx = text.find(substring, start)
        
        if idx == -1:
            break
            
        end_idx = idx + len(substring)
        results.append((idx, end_idx))
        start = end_idx  # Continue search from the character immediately following this match
        
    return results

if __name__ == '__main__':
    sample_text = "hello world hello universe hello"
    sample_substring = "hello"

    indices = find_substring_indices(sample_text, sample_substring)

    print(f'Searching "{sample_substring}" in "{sample_text}":')
    
    for start_idx, end_idx in indices:
        # Extract the matched part to verify correctness during display
        match_content = sample_text[start_idx:end_idx]
        formatted_match = f"Indices ({start_idx}, {end_idx}) -> '{match_content}'"
        print(formatted_match)