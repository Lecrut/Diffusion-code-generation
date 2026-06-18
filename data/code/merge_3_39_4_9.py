def split_by_delimiters(phrase: str, delimiters: set) -> list:
    """
    Splits a phrase into contiguous segments based on a given set of delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set containing single-character strings representing the delimiters.
        
    Returns:
        list: A list of non-empty substrings separated by any of the specified delimiters.
              Empty segments resulting from consecutive or edge delimiters are excluded unless 
              they represent meaningful content based on standard splitting behavior where empty 
              results between separators are typically omitted in such context, but here we include 
              them if they exist strictly as per contiguous segment definition after removal of delimiters.
              
    Note: This implementation treats the problem as replacing all delimiter characters with a single 
          separator and then splitting, effectively ignoring multiple consecutive delimiters unless 
          specific edge cases are intended. However, to match "contiguous segments separated by those",
          we will split on any occurrence of the delimiters, treating them purely as separators that break continuity.
    """
    if not phrase:
        return []

    # Replace all delimiter characters with a single common separator (e.g., '|') for consistent splitting logic
    normalized_phrase = ''.join(char if char not in delimiters else '|' for char in phrase)
    
    parts = [segment for segment in normalized_phrase.split('|')]
    
    # Filter out empty strings that may result from leading/trailing/surrounding delimiters or consecutive ones,
    # unless the requirement implies keeping them. Given "contiguous segments separated by", 
    # standard interpretation excludes pure separator artifacts if no content exists between them.
    return [part for part in parts if part]

if __name__ == '__main__':
    phrase = "Hello.World@@End"
    delimiters_set = {'.', '@'}
    
    result = split_by_delimiters(phrase, delimiters_set)
    print(result)  # Expected output: ['Hello', 'World', 'End']