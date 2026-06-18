def find_substring_indices(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices where `substring` appears in `text`.
    
    Args:
        text (str): The larger text to search within.
        substring (str): The specific substring to find occurrences of.
        
    Returns:
        list[tuple[int, int]]: A list of tuples containing the start and end indices 
                              for each occurrence of `substring`. Indices are 0-based,
                              where end is exclusive. If no matches found, returns an empty list.

    Raises:
        ValueError: If either input is not a string or if substring exceeds text length.
    """
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both inputs must be strings.")
    
    if len(substring) > len(text):
        return []

    matches = []
    start_index = 0
    
    while True:
        # Find the next occurrence of substring starting from current position
        index = text.find(substring, start_index)
        
        if index == -1:
            break
            
        end_index = index + len(substring)
        matches.append((index, end_index))
        
        # Ensure we don't miss overlapping occurrences by continuing the search 
        # from the current 'end' position unless there are overlaps.
        # To catch all overlaps (e.g., in "aaaa" searching for "aa"), increment start by 1.
        if index + len(substring) < len(text):
            start_index = index + 1
        else:
            break

    return matches

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    
    text_sample_1 = "ababa"
    substring_sample_1 = "aba"
    
    result_1 = find_substring_indices(text_sample_1, substring_sample_1)
    
    print(f"Searching for '{substring_sample_1}' in {text_sample_1!r}:")
    if not result_1:
        print("No matches found.")
    else:
        for start_idx, end_idx in result_1:
            extracted = text_sample_1[start_idx:end_idx]
            print(f"Match at index {start_idx}-{end_idx} (substring: '{extracted}')")

    # Additional test case with overlapping occurrences
    text_sample_2 = "aaaaa"
    substring_sample_2 = "aa"
    
    result_2 = find_substring_indices(text_sample_2, substring_sample_2)
    
    print(f"\nSearching for '{substring_sample_2}' in {text_sample_2!r}:")
    if not result_2:
        print("No matches found.")
    else:
        for start_idx, end_idx in result_2:
            extracted = text_sample_2[start_idx:end_idx]
            print(f"Match at index {start_idx}-{end_idx} (substring: '{extracted}')")

    # Test case with no occurrences
    text_sample_3 = "hello world"
    substring_sample_3 = "xyz"
    
    result_3 = find_substring_indices(text_sample_3, substring_sample_3)
    
    print(f"\nSearching for '{substring_sample_3}' in {text_sample_3!r}:")
    if not result_3:
        print("No matches found.")
    else:
        for start_idx, end_idx in result_3:
            extracted = text_sample_3[start_idx:end_idx]
            print(f"Match at index {start_idx}-{end_idx} (substring: '{extracted}')")