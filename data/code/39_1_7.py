import re

def extract_pattern(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a regex pattern from text using Python's 're' module.

    Args:
        text (str): The input string to search within.
        pattern (str): The regular expression pattern to match.

    Returns:
        list[str]: A list of strings containing the matched substrings in order found.
    
    Note: This implementation uses `re.findall()` which inherently handles non-overlapping matches,
          making it optimal for this requirement without manual loop management or lookaheads that might be inefficient.
    """
    try:
        compiled_pattern = re.compile(pattern)
        return compiled_pattern.findall(text)
    except re.error as e:
        # In case of invalid regex pattern, raise the error to fail fast and provide clear feedback
        raise ValueError(f"Invalid regular expression pattern: {e}") from None

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly in the plain. Don't let it blow your hat."
    # Pattern matches words that start with a vowel and end with an 'n' or 'l', case-insensitive
    target_pattern = r'\b[a-z]*[aeiou]([^a-zA-Z]|$)' 
    
    try:
        results = extract_pattern(sample_text, re.escape(target_pattern)) 
        print(f"Matches found for pattern '{re.escape(target_pattern)}':")
        for item in results:
            if isinstance(item, tuple):
                # handle cases where findall returns tuples (though standard non-group patterns return strings)
                pass
            else:
                print("Matched text:", item) 
    except ValueError as ve:
        print(f"Error during pattern matching: {ve}")