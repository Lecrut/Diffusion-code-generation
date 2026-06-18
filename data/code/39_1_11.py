import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regex.
    
    Args:
        text (str): The string to search within.
        pattern (str): The regular expression pattern to match.
        
    Returns:
        List[str]: A list containing the matched substrings in order of appearance.
    """
    matches = re.findall(pattern, text)
    return matches

if __name__ == '__main__':
    sample_text = "The rain in Spain stays mainly in the plain."
    pattern_to_find = r"ain"
    
    results = extract_pattern_occurrences(sample_text, pattern_to_find)
    
    print(f"Input text: {sample_text}")
    print(f"Pattern used: {pattern_to_find}")
    print("Matches found:")
    for match in results:
        print(match)