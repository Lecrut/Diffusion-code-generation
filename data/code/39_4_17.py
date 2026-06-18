def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into contiguous segments based on a set of delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set containing single-character strings representing the delimiters.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any character in the delimiters set.
                   Empty segments resulting from consecutive or leading/trailing delimiters are excluded,
                   unless an empty string is explicitly requested (not implemented per standard behavior).
    
    Example:
        phrase = "a,b;c", delimiters={'.', ',', ';'} -> ['a', 'b']
        Note: In this example, only ',' and ';' are in the set. '.' is not a delimiter here.
        If we use {'.,;'}, result would be ['a', 'b'].
    """
    if not phrase or delimiters == {}:
        return []

    # Normalize input to ensure consistent handling (though inputs should already be correct types)
    normalized_phrase = str(phrase)
    
    segments = []
    current_segment = []
    
    for char in normalized_phrase:
        if char in delimiters:
            if current_segment:
                segments.append("".join(current_segment))
                current_segment = []
        else:
            current_segment.append(char)
            
    # Append the last segment if it's not empty
    if current_segment:
        segments.append("".join(current_segment))

    return segments

if __name__ == '__main__':
    sample_phrase = "Hello, World! How are you?"
    delimiters_set = {',', '!', '?'}
    
    result_segments = split_by_delimiters(sample_phrase, delimiters_set)
    
    print("Input phrase:", repr(sample_phrase))
    print("Delimiter set:", delimiters_set)
    print("Segments found:")
    for i, segment in enumerate(result_segments):
        print(f"  {i}: {repr(segment)}")