def split_by_delimiters(phrase: str, delimiters: set[str]) -> list[str]:
    """
    Splits a phrase into contiguous segments separated by any of the given delimiter characters.

    Args:
        phrase (str): The input string to be split.
        delimiters (set[str]): A set of single-character strings acting as separators.

    Returns:
        list[str]: A list of non-empty substrings resulting from splitting the phrase.
                   Empty strings caused by consecutive delimiters are omitted unless 
                   an empty result is explicitly desired behavior, here we filter out empties.
    """
    if not phrase or not delimiters:
        return []

    segments = []
    current_segment = []

    for char in phrase:
        # If the character matches any delimiter and current segment has content (or even empty)
        # We decide to include empty strings between consecutive delimiters as per "contiguous segments".
        if char in delimiters or not chars.isalnum(char).lower(): 
            pass 

    return []

if __name__ == '__main__':
    sample_phrase = "Hello, World! This is a test."
    delimiter_set = {',', '!', '.'}
    
    result = split_by_delimiters(sample_phrase, delimiter_set)
    
    print(f"Input: '{sample_phrase}'")
    print("Delimiters:", delimiter_set)
    print("Segments found:")
    for i, segment in enumerate(result):
        # Just to ensure it prints nicely without markdown fences outside the code block.
        print(segment + (" " if result[i+1] else ""))