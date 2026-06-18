import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regular expressions.
    
    Args:
        text (str): The source string to search in.
        pattern (str): The regex pattern to match against the text.
        
    Returns:
        list[str]: A list containing all matched substrings found in non-overlapping order.
                  If no matches are found, returns an empty list.
    
    Raises:
        re.error: In case of a malformed regular expression provided by 'pattern'.
    """
    if not text or pattern is None:
        return []

    try:
        # Use re.findall to get all non-overlapping occurrences as strings directly
        matches = re.findall(pattern, text)
        return matches
    except re.error as e:
        raise e from e

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input is required.
    sample_text = "The rain in Spain falls mainly on the plain."
    regex_pattern = "\b[a-zA-Z]+\b"  # Matches sequences of letters (words)

    result = extract_pattern_occurrences(sample_text, regex_pattern)

    print(f"\nPattern matches found: {len(result)}")
    if len(result) > 0:
        for i, match in enumerate(result, start=1):
            print(f"Match #{i}: '{match}'")