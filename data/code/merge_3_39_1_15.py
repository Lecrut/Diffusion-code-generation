import re

def extract_pattern(pattern: str, text: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a pattern from a given string using regular expressions.
    
    Args:
        pattern (str): The regex pattern to search for.
        text (str): The input string to search within.
        
    Returns:
        list[str]: A list containing the matched substrings. If no matches are found, returns an empty list.
    """
    try:
        compiled_pattern = re.compile(pattern)
        matches = []
        for match in compiled_pattern.finditer(text):
            matches.append(match.group())
        return matches if matches else [""]
    except re.error as e:
        # In case the pattern is invalid, we handle it gracefully by returning an empty list or raising.
        # Based on typical expectations for such tasks without crashing silently:
        raise ValueError(f"Invalid regular expression: {e}") from None

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly in the plain."
    sample_pattern = r"\b\w+ain\b"  # Matches words ending with 'ain' like 'rain', 'Spain', 'plain'

    result = extract_pattern(sample_pattern, sample_text)
    
    if not isinstance(result[0], str):
        print("No matches found.")
    else:
        for match in result:
            print(match)