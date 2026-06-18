def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into contiguous segments based on a set of delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set containing single-character strings representing the delimiters.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any of the provided delimiters.
                   Consecutive delimiters are treated as a single separator, and leading/trailing 
                   segments resulting from consecutive or edge delimiters are omitted if empty.
    
    Example:
        >>> phrase = "a,b,c"
        >>> delims = {','}
        >>> split_by_delimiters(phrase, delims)
        ['a', 'b', 'c']
        
        >>> phrase = "...hello..."
        >>> delims = {'.'}
        >>> split_by_delimiters(phrase, delims)
        ['', '', 'hello', '', '']  # Note: Empty strings are included if they exist between non-consecutive splits.
    """
    result = []
    
    current_segment = ""
    
    for char in phrase:
        if char in delimiters:
            if current_segment != "":
                result.append(current_segment)
                current_segment = ""
        else:
            current_segment += char
            
    # Append the last segment if it's not empty (or handle trailing delimiter logic based on strictness)
    # Based on standard split behavior where consecutive delimiters create empty strings unless specified otherwise,
    # we will include non-empty segments. If the requirement implies ignoring empty results from edge cases:
    if current_segment != "":
        result.append(current_segment)

    return result

if __name__ == '__main__':
    sample_phrase = "Hello...World!!..."
    delimiters_set = {'.', '!', '?', ','}  # Set of delimiter characters
    
    segments = split_by_delimiters(sample_phrase, delimiters_set)
    
    print("Input phrase:", repr(sample_phrase))
    print("Delimiters:", delimiters_set)
    print("Segments found:")
    for i, segment in enumerate(segments):
        print(f"  [{i}]: {repr(segment)}")