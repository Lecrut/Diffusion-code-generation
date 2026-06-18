import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific regex pattern from text.
    
    This function uses Python's `re` module to find and return every match 
    found within the input string as a list of strings. It handles overlapping patterns
    by ensuring matches are consumed sequentially (non-overlapping).

    Args:
        text (str): The input string to search within.
        pattern (str): The regex pattern to search for. Must be a valid regular expression.

    Returns:
        list[str]: A list containing all non-overlapping matched strings in the order of discovery.
    
    Raises:
        re.error: If the provided `pattern` is not a valid regular expression.
    """
    try:
        compiled_pattern = re.compile(pattern)
        return [match.group(0) for match in compiled_pattern.finditer(text)]
    except re.error as e:
        raise ValueError(f"Invalid regex pattern: {e}") from e

if __name__ == '__main__':
    sample_text = "The rain in Spain. Sun shines bright."
    search_term = r"\b\S+ain\b|\bsun\s+\w+"
    
    matches = extract_pattern_occurrences(sample_text, search_term)
    
    print(f"Input text: '{sample_text}'")
    print(f"Pattern used (raw): {search_term}")
    print(f"All matched occurrences:\n{matches}")