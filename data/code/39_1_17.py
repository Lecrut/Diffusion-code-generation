import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regular expressions.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to match against the text.

    Returns:
        List[str]: A list containing all matched substrings in order of appearance.
    
    Note:
        Uses re.findall() which naturally returns non-overlapping matches from left to right.
    """
    if not isinstance(text, str) or not pattern:
        return []
    
    try:
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.findall(text)
        # If the pattern contains groups, findall returns tuples/lists of groups; 
        # otherwise it returns strings. We join them if a match is found to ensure list elements are consistent.
        result_list = []
        for m in matches:
            if isinstance(m, tuple):
                result_list.append(''.join(str(x) for x in m))
            else:
                result_list.append(str(m))
        return result_list
    except re.error as e:
        # In a real scenario, we might want to raise this explicitly or handle it differently.
        # For this task, returning an empty list on invalid pattern is safe behavior for extraction logic.
        print(f"Invalid regular expression provided: {e}", file=__import__('sys').stderr)
        return []

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly in the plain."
    search_pattern = r"\b\w+ain\b"  # Matches words ending with 'ain' (rain, Spain, main, plain)

    results = extract_pattern_occurrences(sample_text, search_pattern)

    print("Original Text:", sample_text)
    print(f"Pattern: {search_pattern}")
    print("Matches found:")
    for i, match in enumerate(results, 1):
        print(f"{i}. \"{match}\"")