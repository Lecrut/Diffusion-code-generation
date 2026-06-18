import re

def extract_pattern_occurrences(pattern: str, text: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a pattern from the given input string.
    
    Args:
        pattern (str): The regex pattern to search for.
        text (str): The string in which to search for matches.
        
    Returns:
        list[str]: A list containing each matched substring found in order.
    """
    compiled_pattern = re.compile(pattern)
    return compiled_pattern.findall(text)

if __name__ == '__main__':
    sample_text = "The rain was spilling into the canal."
    sample_pattern = "(?:r|a)"  # Matches any 'r' or 'a', non-overlapping
    
    matches = extract_pattern_occurrences(sample_pattern, sample_text)
    
    print(f"Pattern: {sample_pattern}")
    print(f"Text: '{sample_text}'")
    print(f"Matches found ({len(matches)}):")
    for i, match in enumerate(matches, 1):
        print(f"{i}. '{match}'")