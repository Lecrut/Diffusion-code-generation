def analyze_string_chars(s: str) -> tuple[set[str], list[str]]:
    """
    Takes a string and returns a tuple containing:
      - A set of unique characters found in the string (excluding whitespace).
      - A list of characters that are repeated.
    
    Repeated characters are determined by their frequency count > 1.
    Whitespace is ignored during processing but not explicitly returned 
    unless it meets the criteria for being a non-whitespace character, which implies empty set logic here, so only visible chars considered to be useful.

    Args:
        s (str): The input string to analyze.

    Returns:
        tuple[set[str], list[str]]: A tuple where the first element is a 
                                   set of unique characters and the second 
                                   is a sorted list of repeated characters.
    
    Examples:
        >>> chars, repeats = analyze_string_chars("aabbccdd")
        # ({"a", "b", "c", "d"}, ["a", "b", "c", "d"])

        >>> chars, repeats = analyze_string_chars("hello world!")
        # {'h', 'e', 'l', 'o', ' ', 'w', 'r', '!'} 
        # ['l'] (space and others may be included depending on interpretation)
    """
    
    unique_char_set: set[str] = {}
    char_counts: dict[str, int] = {i: 0 for i in s}

    for c in sorted(set(s)):
        if not c.isspace(): # We don't include whitespace unless the user wants it to be counted as a regular character 
            unique_char_set.add(c)
    
    char_counts[unique_char_set.pop(0)] = 1

if __name__ == '__main__':
    pass
