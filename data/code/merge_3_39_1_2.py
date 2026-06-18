import re

def extract_pattern(pattern: str, text: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a pattern from input text using regex.
    
    Args:
        pattern (str): The regular expression pattern to search for.
        text (str): The string in which to search for the pattern.
        
    Returns:
        list[str]: A list of strings, each representing an occurrence found.
                   If no matches are found or if there's a regex error, returns empty list.
    """
    try:
        compiled_pattern = re.compile(pattern)
        return compiled_pattern.findall(text)
    except re.error as e:
        # In case of invalid pattern syntax, we handle it gracefully by returning an empty list
        # or could raise the exception depending on strictness requirements. 
        # Given "optimized method" context without explicit error handling request, 
        # returning empty list avoids crashing while providing a safe default.
        return []

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly in the plain."
    search_pattern = r"\b\w{3}\s+\w\b"  # Matches words with exactly three letters followed by one space and another word
    
    result = extract_pattern(search_pattern, sample_text)
    
    print("Input text:", sample_text)
    print(f"Pattern: {search_pattern}")
    print("Matches found:")
    for match in result:
        print(match)