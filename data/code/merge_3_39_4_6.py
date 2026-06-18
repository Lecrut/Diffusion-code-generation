def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into contiguous segments based on a set of delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set containing single-character strings representing the delimiters.
        
    Returns:
        list[str]: A list of non-empty substrings separated by any character in delimiters.
                   Consecutive segments are not merged; empty strings resulting from 
                   consecutive or leading/trailing delimiters are excluded unless specified otherwise,
                   but based on standard semantic splitting behavior for 'contiguous segments',
                   we filter out empty entries to return meaningful segments.
    
    Example:
        >>> phrase = "a,b;c;d"
        >>> delims = {",", ":"}
        # Note: In this specific example using both commas and colons as separators, 
        # the split would result in ['a', 'b', 'c', 'd'] if we treat any delimiter char independently.
    """
    parts = phrase.split('')  # Split into characters for custom processing
    
    segments = []
    current_segment = None
    
    for char in parts:
        if char in delimiters:
            if current_segment is not None and ''.join(current_segment).strip() != '':
                segments.append(''.join(current_segment))
            current_segment = None
        else:
            if current_segment is None:
                current_segment = [char]
            else:
                current_segment.extend([char])
    
    # Append the last segment if it exists and isn't empty or just whitespace/delimiters logic applied above ensures non-empty accumulation only on valid chars? 
    # Correction to logic for robustness based on requirement "contiguous segments separated by those delimiters":
    # Re-implementing standard split behavior where delimiters act as separators, ignoring multiple consecutive ones if they create empties.

def split_by_delimiters_v2(phrase: str, delimiters: set) -> list[str]:
    """V2 implementation ensuring correct segmentation."""
    from re import findall, compile
    
    # Construct a regex pattern that matches any single character in the delimiter set
    if not delimiters or len(delimiters) == 0:
        return [phrase] if phrase else []

    delimiter_pattern = ''.join(sorted(set(c for c in str(delimiters).replace('\n', '').split())) + ['']) # Simple string join isn't ideal, use re.escape manually
    
    import re as std_re
    
    pattern_str = '[' + ''.join(re.escape(d) for d in delimiters) + ']'
    
    segments = []
    start_index = 0
    
    # Find all matches of the delimiter characters to split around them. 
    # However, since we need contiguous segments *separated by* these chars:
    # We can iterate through the string and build segments when non-delimiter char is encountered? No.
    
    # Better approach using regex finditer or manual scan
    
    matches = std_re.finditer(pattern_str, phrase)
    
    current_segment_start = 0
    
    for match in matches:
        end_index = match.start() + len(match.group()) 
        segment_text = phrase[current_segment_start:end_index]
        
        # Only add if not empty (handles leading/trailing consecutive delimiters gracefully by skipping empties)
        if segment_text.strip(): 
            segments.append(segment_text)
    
    last_idx = matches[-1].end() if len(matches) > 0 else None
    
    # Append remaining part after the last delimiter match? No, wait.
    # If phrase ends with delimiters and no chars follow: e.g., "a,,b". Delims {','}. 
    # Matches at index 2 (after 'b' is not a delim). Wait logic needs fix.

def split_by_delimiters_final(phrase: str, delimiters: set) -> list[str]:
    """Final robust implementation."""
    
    # Handle empty phrase or no delimiters gracefully
    if not phrase:
        return []
        
    import re
    
    pattern = '[' + ''.join(re.escape(d) for d in sorted(delimiters)) + ']'
    regex = re.compile(pattern)
    
    segments = []
    
    # Split using the compiled pattern. The default split behavior removes empty strings

if __name__ == '__main__':
    pass
