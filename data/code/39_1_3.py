import re

def extract_patterns(text: str, pattern: str) -> list[str]:
    """
    Extract all non-overlapping occurrences of a specific pattern from input text using regular expressions.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to match.

    Returns:
        List[str]: A list containing all matched substrings in the order they appear.
    """
    matches = re.findall(pattern, text)
    return matches

if __name__ == '__main__':
    sample_text = "The rain in Spain falls mainly on the plain."
    pattern_to_search = r"ain"

    result = extract_patterns(sample_text, pattern_to_search)

    print(f"\nInput Text:\n{sample_text}\n")
    print(f"Regex Pattern: {pattern_to_search}")
    print("Extracted Matches:")
    
    if not result:
        print("(No matches found)")
    else:
        for i, match in enumerate(result, 1):
            print(f"{i}. \"{match}\"")