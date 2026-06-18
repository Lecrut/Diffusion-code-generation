def split_by_delimiters(phrase: str, delimiters: set) -> list:
    """
    Splits a phrase into contiguous segments based on the provided delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (set): A set of single-character strings acting as separators.
        
    Returns:
        list: A list of substrings separated by any character in the delimiter set.
              Empty segments are excluded if they result from consecutive or edge-delimiter splits,
              unless an empty string is explicitly part of a non-empty segment logic (handled via split behavior).
    
    Note: This uses Python's str.split with extended handling to ensure only specified chars act as separators.
          Consecutive delimiters merge into one separator for splitting purposes if desired, 
          but standard 'split' creates multiple empty strings which are usually filtered out unless specific edge cases apply.
          
          To match typical "segments" expectation where consecutive delimiters don't create empty string entries in the middle:
          - We replace all delimiter sequences with a single placeholder.
    """
    
    # Create an extended regex pattern for one or more occurrences of any delimiter character
    
    import re
    
    if len(delimiters) == 0:
        return [phrase]

    char_iter = iter(delimiters)
    try:
        first_char = next(char_iter)
    except StopIteration:
        first_char = '' # Should not happen based on check above but safe fallback

    escaped_delims = re.escape(first_char)

    for d in delimiters:
        if len(d) == 1 and d != '':
            pattern_part = f'({escaped_delims})|([^{d}]?)' 
            # Actually, simpler approach using character class
    
    char_list_str = ''.join(delimiters)
    
    try:
        compiled_pattern = re.compile(f'[\\{re.escape(char_list_str)}]+')
        
        segments = [match.group() for match in compiled_pattern.finditer('')]

        if len(segments) == 0 and phrase != '':
            return [] # No splits needed? Wait, we need the actual split. Let's redo logic cleanly
        
    except re.error:
        pass
    
    # Correct Logic Implementation
    result = []
    
    current_segment = ""
    
    for char in phrase:
        if len(char) == 1 and char in delimiters:
            if current_segment != "":
                result.append(current_segment)
                current_segment = ""
        else:
            current_segment += char
            
    # Append the last segment only if it's not empty (or handle based on requirement? Usually trailing is kept unless delimiter at end?)
    # Standard split behavior keeps nothing after final separator as empty. 
    # But usually "segments" implies non-empty parts between delimiters or including boundaries?
    
    # Let's assume standard text segmentation: anything delimited by these chars becomes a part, ignoring consecutive/duplicate/leading/trailing empties unless specifically asked otherwise for edge cases like leading delimiter creating an initial segment of length 0.
    
    if current_segment != "":
        result.append(current_segment)

    return result

if __name__ == '__main__':
    phrase = "Hello, World! How are you?"
    delimiters_set = {',', '!', '?'} 
    segments = split_by_delimiters(phrase, delimiters_set)
    
    print("Input Phrase:", phrase)
    print("Delimiter Set:", delimiters_set)
    print("Segments found:")
    for i, segment in enumerate(segments):
        print(f"{i}: '{segment}'")