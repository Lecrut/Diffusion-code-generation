import re

def extract_occurrences(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from a given input string using regular expressions.

    Args:
        text (str): The input string to search within.
        pattern (str): The regex pattern to match against the text.

    Returns:
        list[str]: A list containing all non-overlapping matches found in the text.
    """
    return re.findall(pattern, text)

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes without user input or command-line arguments
    test_text = "The rain in Spain falls mainly in the plain."
    regex_pattern = r"\b[a-z]{3}\s+\w\.\s"  # Matches words like "ain", "ain", etc. followed by space and word with period

    result = extract_occurrences(test_text, regex_pattern)
    
    print(f"Mentions of '{regex_pattern.strip()}':")
    for match in result:
        print(match.strip())