def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into contiguous segments based on a given set of delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set containing single-character strings representing the delimiters.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any of the provided delimiters.
                   Consecutive delimiters are treated as a single separator, and leading/trailing 
                   empty segments resulting from adjacent or edge delimiters are excluded unless 
                   they contain actual content (i.e., only non-empty segments are returned).
    
    Example:
        >>> phrase = "a,b,c"
        >>> delims = {','}
        >>> split_by_delimiters(phrase, delims)
        ['a', 'b', 'c']
        
        >>> phrase = "...hello..."
        >>> delims = {'.', '_'}
        >>> split_by_delimiters(phrase, delims)
        ['hello']
    """
    if not phrase:
        return []

    result = []
    current_segment = []

    for char in phrase:
        # Check if the character is a delimiter (case-sensitive based on input set)
        if char in delimiters:
            # If we have accumulated characters, add them to the result list
            if current_segment:
                result.append("".join(current_segment))
                current_segment = []
        else:
            # Accumulate non-delimiter characters into the current segment
            current_segment.append(char)

    # Append any remaining content after the last delimiter or end of string
    if current_segment:
        result.append("".join(current_segment))

    return result

if __name__ == '__main__':
    sample_phrase = "apple,banana;orange_mango"
    sample_delimiters = {',', ';', '_'}

    segments = split_by_delimiters(sample_phrase, sample_delimiters)
    
    print("Input phrase:", repr(sample_phrase))
    print("Delimiters:", sample_delimiters)
    print("Segments found:")
    for i, segment in enumerate(segments):
        print(f"  {i+1}. {repr(segment)}")