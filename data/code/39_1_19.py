import re

def extract_pattern_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regular expressions.
    
    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to match against the text.
        
    Returns:
        list[str]: A list containing all matched substrings in order of appearance.
    """
    matches = re.findall(pattern, text)
    return matches

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_text = "The rain in Spain falls mainly in the plain."
    search_pattern = r"\b\w+\bin\b"  # Matches words ending with 'in' (case-insensitive by default unless specified)

    result = extract_pattern_occurrences(test_text, search_pattern)
    
    print("Input text:", test_text)
    print(f"Pattern: {search_pattern}")
    print("Matches found:")
    for match in result:
        print(match)