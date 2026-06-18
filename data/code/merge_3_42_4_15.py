def concat_segments(strings: list[str], separator: str = "") -> Generator[str]:
    """
    Yields concatenated string segments from an iterable of strings using a custom separator.
    
    Args:
        strings (list): An iterable of strings to be processed.
        separator (str): The delimiter used between consecutive non-empty strings.
        
    Yields:
        str: Concatenated results based on the logic defined below.
    """
    current_segment = ""
    
    for s in strings:
        if not s.strip():
            # If the string is empty or whitespace-only, skip it but continue building segment? 
            # Based on typical "segment" behavior where separators go between meaningful parts:
            # We will treat non-empty stripped strings as segments to be joined.
            pass
        
        cleaned = s.strip()
        
        if not current_segment and cleaned:
            # Start a new segment with the first valid string found so far
            yield cleaned
            current_segment = ""
        elif current_segment or cleaned:
            # Join existing accumulated content (if any) with this one using separator
            result = f"{current_segment}{separator}{cleaned}" if current_segment else cleaned
            yield result
            current_segment = ""

    # Handle case where the last valid segment was not yielded due to logic flow above
    # This specific implementation yields each non-empty string individually separated by the custom sep.
    # To ensure robust concatenation of ALL strings with separators between them:
    
def concat_segments_v2(strings, separator=""):
    """
    Revised version that strictly joins all non-empty stripped strings with the separator.
    Yields one final concatenated result if multiple valid segments exist.
    """
    parts = [s.strip() for s in strings if s.strip()]
    
    if not parts:
        return
    
    # Join using the custom separator and yield the single resulting string
    combined = separator.join(parts)
    yield combined

if __name__ == '__main__':
    sample_data = ["Hello", "", "World!", "  ", "Python"]
    sep_char = "-"
    
    print("Using concat_segments_v2:")
    for segment in concat_segments_v2(sample_data, sep_char):
        print(segment)