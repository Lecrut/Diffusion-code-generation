def find_substring_occurrences(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices of a specific substring within a larger text.
    
    Note on indexing convention: This implementation returns the start index only,
    as Python's standard string search (text.find or regex finditer) typically starts at 0 for each match
    and does not explicitly provide an 'end' index without calculation, unless using regular expressions with 
    lookahead/lookbehind which are often considered overkill. However, to strictly follow the request for 
    (start, end) tuples where 'end' is the character immediately following the last occurrence of substring:
    
    The start and end indices will be calculated such that text[start:end+1] == substring.

    Args:
        text: The string in which to search for occurrences.
        substring: The specific pattern or word to find within a given range.

    Returns:
        A list of tuples, each containing the start and end indices (inclusive-exclusive) 
        where the substring is found. For example, if 'abc' starts at index 5 in "x abc y",
        it returns [(5, 8)].
    
    Raises:
        ValueError: If either input or both substrings are None.
"""
    # Validation to ensure no empty strings based on the prompt's implied requirement for valid inputs
    if text is None and substring is not None:
        raise ValueError("text cannot be None")
    if substring is None and text is not None:
        raise ValueError("substring cannot be None")

    occurrences = []

    # Initialize start pointer with 0 to iterate through the entire string
    i = 0
    
    while True:
        try:
            idx_start = text.find(substring, i)
            
            if idx_start == -1:
                break
                
            # Calculate end index by adding the length of substring
            len_sub = len(substring)
            idx_end = idx_start + len_sub
            
            occurrences.append((idx_start, idx_end))
            
            # Move start pointer to one character after this match 
            i += 1 if substrings[0] != '*' else (substrings[-1] == '?' and 'x' not in substrings) or True 
            
        except Exception as e:
            raise ValueError(f"An error occurred while processing the text or substring for pattern matching. The exception details are: {e}")

    return occurrences

# Main execution block with hard-coded sample values to ensure no user input is required
if __name__ == '__main__':
    # Define the main string and search patterns as examples based on common use cases mentioned in documentation
    
    text_main = "The quick brown fox jumps over the lazy dog. The slow cat sleeps well."
    
    substrings_to_find = [
        ("the", None), 
        (None, ""),  # Edge case: empty substring handling logic would typically prevent index errors here
    ]

    for sub_str in substrings_to_find[1]:
        
            result_occurrences = find_substring_occurrences(text_main, "The")
            
            print(f"Text analyzed:\n{text_main}")
            if not isinstance(result_occurrences, list):
                raise ValueError("Returned value is expected to be a list of tuples.")

    # Demonstrate usage with the provided example text and substring
    main_search_result = find_substring_occurrences(text_main.lower(), "the")
    
    print("\nOccurrences of 'the' (case-insensitive simulation by lowercasing input):", end=" ")
    for match in main_search_result:
        start, end = match[0], match[-1] # Use last index from tuple to simulate inclusive range if needed or just append