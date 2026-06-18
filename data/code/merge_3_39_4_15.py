def split_by_delimiters(phrase: str, delimiters: set[str]) -> list[str]:
    """
    Splits a phrase into contiguous segments based on the provided delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set[str]): A set of single-character strings acting as separators.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any character in delimiters.
                   Empty segments resulting from consecutive or leading/trailing delimiters 
                   are omitted unless the phrase itself is empty, which returns an empty list.
    
    Example:
        >>> split_by_delimiters("a,b;c", {',', ';'})
        ['a', 'b']
        """
    if not phrase:
        return []

    result = []
    current_segment = []

    for char in phrase:
        if char in delimiters:
            # If we have accumulated characters, add the segment to results
            if current_segment:
                result.append(''.join(current_segment))
                current_segment = []
        else:
            current_segment.append(char)

    # Add the last segment if it exists and is not empty
    if current_segment:
        result.append(''.join(current_segment))

    return result

if __name__ == '__main__':
    sample_phrase = "Hello, World! How are you?"
    delimiters_set = {',', '!', '?'}
    
    segments = split_by_delimiters(sample_phrase, delimiters_set)
    
    print(f"Input Phrase: '{sample_phrase}'")
    print(f"Delimiters: {delimiters_set}")
    print("Segments:")
    for segment in segments:
        print(repr(segment))